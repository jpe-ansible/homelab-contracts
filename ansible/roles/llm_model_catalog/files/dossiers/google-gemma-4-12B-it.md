---
type: Model Dossier
title: "google/gemma-4-12B-it"
description: "Upstream and artifact evidence for the shared model policy."
timestamp: "2026-11-22T00:00:00Z"
status: started
---

## 1. Upstream evidence

- Observed: 2026-11-22. [Hub metadata](https://huggingface.co/api/models/google/gemma-4-12B-it).
- Upstream repository created: 2026-05-23 (Hub `createdAt`).
  Release date: UNVERIFIED. Conversion dates do not renew upstream age.
- Upstream creation or release date: 2026-05-23T01:17:15.000Z (`createdAt`),
  [Hub API](https://huggingface.co/api/models/google/gemma-4-12B-it),
  observed 2026-11-22.
- Observed immutable upstream revision: `43c9d014b231474fa7212dbb48a762566c2b255d`.
  [Pinned upstream card](https://huggingface.co/google/gemma-4-12B-it/blob/43c9d014b231474fa7212dbb48a762566c2b255d/README.md).
- License: apache-2.0. [License evidence](https://huggingface.co/google/gemma-4-12B-it/blob/43c9d014b231474fa7212dbb48a762566c2b255d/README.md).
  Additional restrictions: UNVERIFIED.
- Architecture: gemma4_unified (`Gemma4UnifiedForConditionalGeneration`),
  from the Hub `config`.
- Intended task: Text and image-text generation, per the upstream card.
- Role-assigned artifacts: none. The catalog entry is the
  instruction-tuned MLX build below.

## 2. Artifact evidence

### mlx-community/gemma-4-12B-it-4bit

- [Artifact metadata](https://huggingface.co/api/models/mlx-community/gemma-4-12B-it-4bit?blobs=true),
  observed 2026-11-22; artifact repository created 2026-06-03.
- Artifact repository: `mlx-community/gemma-4-12B-it-4bit`.
- Artifact publisher: `mlx-community` (`author`).
- Immutable artifact revision: `73bcf09092aa277861d5a191b989b666f7f32e8f` (`sha`).
- Artifact created date: 2026-06-03T16:19:43.000Z (`createdAt`).
- Evidence observed date: 2026-11-22,
  [Hub API](https://huggingface.co/api/models/mlx-community/gemma-4-12B-it-4bit?blobs=true).
- Quantization recipe: affine 4-bit, group size 64,
  [pinned config](https://huggingface.co/mlx-community/gemma-4-12B-it-4bit/blob/73bcf09092aa277861d5a191b989b666f7f32e8f/config.json),
  observed 2026-11-22.
- Calibration provenance: not applicable; MLX affine 4-bit quantization in
  the pinned config applies no calibration data,
  [pinned config](https://huggingface.co/mlx-community/gemma-4-12B-it-4bit/blob/73bcf09092aa277861d5a191b989b666f7f32e8f/config.json),
  observed 2026-11-22.
- Upstream source revision: not published by converter; the artifact card
  declares no `base_model`.
- Weight files: UNVERIFIED (not enumerated for this revision).
- Maximum positions in the pinned config: 262144 (`text_config.max_position_embeddings`).
  The catalog serves 131072.

## 3. Runtime and memory

- Runtime: `mlx-vlm` serves `gemma4_unified` at the pinned upstream commit.
  Runtime qualification on this host: UNVERIFIED (no model runs yet).
- Memory budget: UNVERIFIED.

## 4. Evaluation and comparison

- Benchmark: MMLU Pro, Gemma 4 12B Unified row of the upstream card,
  instruction-tuned models; score: 77.2; date: 2026-11-22;
  source: <https://huggingface.co/google/gemma-4-12B-it/blob/43c9d014b231474fa7212dbb48a762566c2b255d/README.md>

## 5. Trial status

- Dated promotion decision: UNVERIFIED (no trial run).
- Predeclared acceptance criteria: UNVERIFIED.
- Unresolved fields: runtime qualification, memory budget, task-matched
  comparison, and trial evidence.
