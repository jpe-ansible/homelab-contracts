# apt_cache_client

Shared apt cache client configuration, replacing the apt proxy block that
`ansible-proxmox-apps` used to render inline in its site playbook
(`playbooks/site/01-baseline-infra.yml`).

The cache is an HA pair (tofu `node_services` generates one instance per
always-on node). apt itself supports only a single `Acquire::http::Proxy`
value, so instance selection uses apt's native Proxy-Auto-Detect hook
instead: at every apt run the hook script probes each cache in
`apt_cache_client_urls` order and prints the first live one, or `DIRECT`
so apt fails open when the whole pool is down. An instance (or its node)
going down therefore costs one probe timeout, never apt itself.

The role installs two files — template tasks only, no shell, so `--check`
reports real changes:

| Path | Purpose | Mode |
| --- | --- | --- |
| `/usr/local/bin/apt-proxy-detect` | the Proxy-Auto-Detect hook | 0755 |
| `/etc/apt/apt.conf.d/00proxy` | registers the hook for the http and https apt sources | 0644 |

The probe is retried — three attempts, one second apart, each a three-second
connect test — because a single short connect test is decided by whatever the
cache happens to be doing at that instant, and during a fleet converge it is
serving every other guest at once. When no cache answers, the hook falls back
to `DIRECT` (kept, because some VLANs do reach upstream) and records the
decision in the log, because other VLANs block outbound 80 and `DIRECT`
there fails with an empty apt reason.

## Input

| Variable | Default | Meaning |
| --- | --- | --- |
| `apt_cache_client_urls` | `tofu_data.cache_proxy_urls.apt_cache` | the cache URLs, probed in list order |

e.g. `["http://cache-a.example.com:3142", "http://cache-b.example.com:3142"]`

The role asserts the list is non-empty and that every entry is an http(s)
URL. The drop-in registers the hook for both the http and the https apt
sources, so an `https://` entry in the list serves https sources unchanged.

## Installation

Pin via `requirements.yml`:

```yaml
roles:
  - name: apt_cache_client
    src: https://github.com/jpe-ansible/homelab-contracts.git
    scm: git
    version: <release tag>
```

## Usage

```yaml
# consumer playbook (guest play; run after inventory_resolve)
- name: Configure the apt cache client
  ansible.builtin.include_role:
    name: apt_cache_client
```

Pass `apt_cache_client_urls` explicitly only to override the published
inventory's list (the tests do this).
