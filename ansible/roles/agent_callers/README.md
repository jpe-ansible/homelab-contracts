# agent_callers

This role loads the canonical harness gateway identity and memory trust-tier
registry from `files/callers.json`. Consumers read this file rather than keep a
second caller list.

Deployment-specific trust changes are JSON deltas. A consumer merges
`deployment.caller_overrides[id].trust_tier` over this file for that caller id.
An id may be owned by either this registry or the Tofu container roster, never
both; consumers assert that the two sources have no collision.

The default tier is `untrusted`, the safe tier for a caller without a more
specific trust assignment.

The `public` tier is for a caller that only ever handles public content, such as a
sandbox that works on public repositories. A consumer may give that tier routes that
retain prompts; it never grants it what `trusted` holds, and a consumer that tests
for `trusted` treats `public` like any other non-trusted tier.

`gateway_key` defaults to `true`; `false` means the caller holds no agentgateway
key, so the consumer seeds no gateway-key secret leaf for it and gives it no
gateway routes or memory bank. Every public-tier caller must set it to `false`.
