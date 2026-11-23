---
type: Model Dossier
title: "Qwen/Qwen3-ASR-1.7B"
description: "Upstream and artifact evidence for the shared model policy."
timestamp: "2026-11-22T00:00:00Z"
status: started
---

## 1. Upstream evidence

- Observed: 2026-11-22. [Hub metadata](https://huggingface.co/api/models/Qwen/Qwen3-ASR-1.7B).
- Upstream repository created: 2026-01-28 (Hub `createdAt`).
  Release date: UNVERIFIED. Conversion dates do not renew upstream age.
- Upstream creation or release date: 2026-01-28T03:22:40.000Z (`createdAt`),
  [Hub API](https://huggingface.co/api/models/Qwen/Qwen3-ASR-1.7B),
  observed 2026-11-22.
- Observed immutable upstream revision: `7278e1e70fe206f11671096ffdd38061171dd6e5`.
  [Pinned upstream card](https://huggingface.co/Qwen/Qwen3-ASR-1.7B/blob/7278e1e70fe206f11671096ffdd38061171dd6e5/README.md).
- License: apache-2.0. [License evidence](https://huggingface.co/Qwen/Qwen3-ASR-1.7B/blob/7278e1e70fe206f11671096ffdd38061171dd6e5/README.md).
  Additional restrictions: UNVERIFIED.
- Architecture: qwen3_asr (automatic speech recognition), per the upstream card.
- Intended task: Automatic speech recognition and language identification.
- Role-assigned artifacts: none. The catalog entry is the MLX build below.

## 2. Artifact evidence

### mlx-community/Qwen3-ASR-1.7B-8bit

- [Artifact metadata](https://huggingface.co/api/models/mlx-community/Qwen3-ASR-1.7B-8bit?blobs=true),
  observed 2026-11-22; artifact repository created 2026-01-29.
- Artifact repository: `mlx-community/Qwen3-ASR-1.7B-8bit`.
- Artifact publisher: `mlx-community` (`author`).
- Immutable artifact revision: `a8379a2e2f9e313c9292cdf1af4055ab56d50d55` (`sha`).
- Artifact created date: 2026-01-29T15:08:03.000Z (`createdAt`).
- Evidence observed date: 2026-11-22,
  [Hub API](https://huggingface.co/api/models/mlx-community/Qwen3-ASR-1.7B-8bit?blobs=true).
- Quantization recipe: affine 8-bit, group size 64,
  [pinned config](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit/blob/a8379a2e2f9e313c9292cdf1af4055ab56d50d55/config.json),
  observed 2026-11-22.
- Calibration provenance: not applicable; MLX affine 8-bit quantization in
  the pinned config applies no calibration data,
  [pinned config](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit/blob/a8379a2e2f9e313c9292cdf1af4055ab56d50d55/config.json),
  observed 2026-11-22.
- Upstream source revision: not published by converter; the artifact card
  declares no `base_model`.
- Weight files: UNVERIFIED (not enumerated for this revision).
- Maximum positions in the pinned config: 65536 (`thinker_config.text_config.max_position_embeddings`).
  The catalog serves 65536.

## 3. Runtime and memory

- Runtime: `mlx-audio` 0.6.5 serves `qwen3_asr` (`stt/models/qwen3_asr`) through
  `POST /v1/audio/transcriptions`. Runtime qualification on this host:
  UNVERIFIED (no model runs yet).
- Memory budget: UNVERIFIED.

## 4. Evaluation and comparison

- Benchmark: LibriSpeech test-clean WER, Qwen3-ASR-1.7B row of the upstream
  card (English); score: 1.63; date: 2026-11-22;
  source: <https://huggingface.co/Qwen/Qwen3-ASR-1.7B/blob/7278e1e70fe206f11671096ffdd38061171dd6e5/README.md>

## 5. Trial status

- Dated promotion decision: UNVERIFIED (no trial run).
- Predeclared acceptance criteria: UNVERIFIED.
- Unresolved fields: runtime qualification, memory budget, task-matched
  comparison, and trial evidence.
