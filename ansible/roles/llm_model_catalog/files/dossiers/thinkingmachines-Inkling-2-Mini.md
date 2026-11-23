---
type: Model Dossier
title: "thinkingmachines/Inkling-2-Mini"
description: "Upstream and artifact evidence for the shared model policy."
timestamp: "2026-11-22T00:00:00Z"
status: started
---

## 1. Upstream evidence

- Observed: 2026-11-22. [Hub metadata](https://huggingface.co/api/models/thinkingmachines/Inkling-2-Mini).
- Upstream repository created: 2026-11-17 (Hub `createdAt`).
  Release date: UNVERIFIED. Conversion dates do not renew upstream age.
- Upstream creation or release date: 2026-11-17T00:26:57.000Z (`createdAt`),
  [Hub API](https://huggingface.co/api/models/thinkingmachines/Inkling-2-Mini),
  observed 2026-11-22.
- Observed immutable upstream revision: `b85c3cfa615fc413cc9af3379f491b963f3b586a`.
  [Pinned upstream card](https://huggingface.co/thinkingmachines/Inkling-2-Mini/blob/b85c3cfa615fc413cc9af3379f491b963f3b586a/README.md).
- License: apache-2.0. [License evidence](https://huggingface.co/thinkingmachines/Inkling-2-Mini/blob/b85c3cfa615fc413cc9af3379f491b963f3b586a/README.md).
  Additional restrictions: UNVERIFIED.
- Architecture: inkling2_loop (Hub tags), image-text-to-text pipeline,
  text output per the card's modalities section.
- Intended task: image and text input with text output, per the Hub pipeline
  tag and the upstream card.
- Role-assigned artifacts: none. The catalog entry is the MLX build below.

## 2. Artifact evidence

### mlx-community/Inkling-2-Mini-4bit

- [Artifact metadata](https://huggingface.co/api/models/mlx-community/Inkling-2-Mini-4bit?blobs=true),
  observed 2026-11-22; artifact repository created 2026-11-20.
- Artifact repository: `mlx-community/Inkling-2-Mini-4bit`.
- Artifact publisher: `mlx-community` (`author`).
- Immutable artifact revision: `9c0e2960609ba7cb40daf92c6f7bf8ed56e1dd62` (`sha`).
- Artifact created date: 2026-11-20T21:41:25.000Z (`createdAt`).
- Evidence observed date: 2026-11-22,
  [Hub API](https://huggingface.co/api/models/mlx-community/Inkling-2-Mini-4bit?blobs=true).
- Quantization recipe: affine 4-bit, group size 64,
  [pinned config](https://huggingface.co/mlx-community/Inkling-2-Mini-4bit/blob/9c0e2960609ba7cb40daf92c6f7bf8ed56e1dd62/config.json),
  observed 2026-11-22.
- Calibration provenance: not applicable; MLX affine 4-bit quantization in
  the pinned config applies no calibration data,
  [pinned config](https://huggingface.co/mlx-community/Inkling-2-Mini-4bit/blob/9c0e2960609ba7cb40daf92c6f7bf8ed56e1dd62/config.json),
  observed 2026-11-22.
- Upstream source revision: not published by converter; the artifact tags
  declare `base_model:thinkingmachines/Inkling-2-Mini`.
- Weight files: UNVERIFIED (not enumerated for this revision).
- Maximum positions in the pinned config: 1048576 (`max_position_embeddings`).
  The catalog serves 131072, a serving choice and not a measured limit.

## 3. Runtime and memory

- Runtime: `mlx-vlm` native server at the pinned nix-ai revision.
  Runtime qualification on this host: UNVERIFIED (no model runs yet).
- Drafter: the upstream repository bundles a DSpark drafter. Pairing with
  this MLX artifact is UNVERIFIED, and this entry does not use it.
  Speculative decoding stays off.
- Memory budget: UNVERIFIED.

## 4. Evaluation and comparison

- Benchmark: AA Index (v5.0), Inkling 2 Mini column of the third-party table
  in the upstream card; score: 20.1; date: 2026-11-22;
  source: <https://huggingface.co/thinkingmachines/Inkling-2-Mini/blob/b85c3cfa615fc413cc9af3379f491b963f3b586a/README.md>

Upstream scores describe the original checkpoint. Converted-artifact fidelity,
local capacity, and trial authorization need their own evidence.

## 5. Trial status

- Dated promotion decision: UNVERIFIED (no trial run).
- Predeclared acceptance criteria: UNVERIFIED.
- Unresolved fields: runtime qualification, memory budget, drafter pairing,
  task-matched comparison, and trial evidence.
