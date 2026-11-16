DOCUMENTATION = r"""
name: dryvist.homelab.secret_path
short_description: Build a validated OpenBao path from named components
description:
  - Builds logical and KV v2 API paths from named OpenBao path components.
  - Validates each caller-provided segment against the secrets arrangement
    schema grammar.
options:
  _input:
    description:
      - Mapping containing the named parts of an ordinary secret, admin secret,
        or config path.
    type: dict
    required: true
  form:
    description:
      - Selects the logical path, mount, mount-relative path, KV v2 data path,
        or KV v2 metadata path.
    type: str
    choices:
      - logical
      - mount
      - path
      - data
      - metadata
    default: logical
"""

EXAMPLES = r"""
- name: Build an ordinary logical path
  vars:
    secret_parts:
      zone: int
      service: example-app
      instance: main
      access: ro
  ansible.builtin.debug:
    msg: "{{ secret_parts | dryvist.homelab.secret_path }}"

- name: Build an admin KV v2 data path
  vars:
    secret_parts:
      zone: ext-saas
      service: example-app
      instance: main
      scope: owner
  ansible.builtin.debug:
    msg: "{{ secret_parts | dryvist.homelab.secret_path(form='data') }}"

- name: Build a config metadata path
  vars:
    secret_parts:
      config: true
      service: example-app
      instance: main
  ansible.builtin.debug:
    msg: "{{ secret_parts | dryvist.homelab.secret_path(form='metadata') }}"
"""

RETURN = r"""
_value:
  description:
    - The validated path in the requested form.
  type: str
  returned: always
  sample: int/example-app/main/ro
"""

import re
from collections.abc import Mapping

from ansible.errors import AnsibleFilterError


_SEGMENT_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")
_RESERVED_ZONES = frozenset(
    {"admin", "config", "state", "sys", "auth", "identity", "cubbyhole", "secret"}
)
_ACCESS_VALUES = ("ro", "rw", "self")
_SCOPE_VALUES = ("admin", "management", "owner", "root")
_FORMS = ("logical", "mount", "path", "data", "metadata")


def secret_path(value: object, form: str = "logical") -> str:
    """Build a validated OpenBao KV v2 path from its named components."""
    if not isinstance(value, Mapping):
        raise AnsibleFilterError("input must be a mapping of named path parts")

    allowed_keys = {"zone", "service", "instance", "access", "scope", "config"}
    for key in value:
        if not isinstance(key, str) or key not in allowed_keys:
            raise AnsibleFilterError(
                f"unknown input key {key!r}: only zone, service, instance, "
                "access, scope, and config are allowed"
            )

    if not isinstance(form, str) or form not in _FORMS:
        raise AnsibleFilterError(
            "form must be one of logical, mount, path, data, or metadata"
        )

    if "config" in value:
        if value["config"] is not True:
            raise AnsibleFilterError("config must be true to select the config form")

        extra_key = next(
            (
                key
                for key in value
                if key not in {"config", "service", "instance"}
            ),
            None,
        )
        if extra_key is not None:
            raise AnsibleFilterError(
                f"{extra_key!r} is not allowed when config is true; "
                "config paths accept only config, service, and instance"
            )

        for key in ("service", "instance"):
            if key not in value:
                raise AnsibleFilterError(
                    f"{key} is required for config paths"
                )

        mount = "config"
        parts = ("service", "instance")
    else:
        selectors = tuple(key for key in ("access", "scope") if key in value)
        if len(selectors) == 0:
            raise AnsibleFilterError(
                "access or scope is required; exactly one must be provided"
            )
        if len(selectors) == 2:
            raise AnsibleFilterError(
                "access and scope are both present; exactly one may be provided"
            )

        for key in ("zone", "service", "instance"):
            if key not in value:
                raise AnsibleFilterError(f"{key} is required for secret paths")

        zone = value["zone"]
        if not isinstance(zone, str) or _SEGMENT_PATTERN.fullmatch(zone) is None:
            raise AnsibleFilterError(
                "zone must be a string matching the segment pattern "
                "^[a-z0-9][a-z0-9-]*$"
            )
        if zone in _RESERVED_ZONES:
            raise AnsibleFilterError("zone must not be a reserved mount name")

        if selectors[0] == "access":
            if (
                not isinstance(value["access"], str)
                or value["access"] not in _ACCESS_VALUES
            ):
                raise AnsibleFilterError("access must be one of ro, rw, or self")
            mount = zone
            parts = ("service", "instance", "access")
        else:
            if (
                not isinstance(value["scope"], str)
                or value["scope"] not in _SCOPE_VALUES
            ):
                raise AnsibleFilterError(
                    "scope must be one of admin, management, owner, or root"
                )
            mount = "admin"
            parts = ("zone", "service", "instance", "scope")

    for key in parts:
        if key in {"access", "scope"}:
            continue
        segment = value[key]
        if (
            not isinstance(segment, str)
            or _SEGMENT_PATTERN.fullmatch(segment) is None
        ):
            raise AnsibleFilterError(
                f"{key} must be a string matching the segment pattern "
                "^[a-z0-9][a-z0-9-]*$"
            )

    path = "/".join(value[key] for key in parts)
    if form == "mount":
        return mount
    if form == "path":
        return path
    if form == "data":
        return f"{mount}/data/{path}"
    if form == "metadata":
        return f"{mount}/metadata/{path}"
    return f"{mount}/{path}"


class FilterModule:
    """Expose the secret_path filter to Ansible."""

    def filters(self) -> dict[str, object]:
        return {"secret_path": secret_path}
