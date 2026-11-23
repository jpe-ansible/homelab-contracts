---
type: Model Dossier
title: "inclusionAI/Ming-3.0-tts-0.5B"
description: "Upstream and artifact evidence for the shared model policy."
timestamp: "2026-11-22T00:00:00Z"
status: started
---

## 1. Upstream evidence

- Observed: 2026-11-22. [Hub metadata](https://huggingface.co/api/models/inclusionAI/Ming-3.0-tts-0.5B).
- Upstream repository created: 2026-09-22 (Hub `createdAt`).
  Release date: UNVERIFIED. Conversion dates do not renew upstream age.
- Upstream creation or release date: 2026-09-22T12:46:58.000Z (`createdAt`),
  [Hub API](https://huggingface.co/api/models/inclusionAI/Ming-3.0-tts-0.5B),
  observed 2026-11-22.
- Observed immutable upstream revision: `ffd36ab5764c39c7e5565dfed66a3aeeced58ab9`.
  [Pinned upstream card](https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B/blob/ffd36ab5764c39c7e5565dfed66a3aeeced58ab9/README.md).
- License: mit. [License evidence](https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B/blob/ffd36ab5764c39c7e5565dfed66a3aeeced58ab9/README.md).
  Additional restrictions: UNVERIFIED.
- Architecture: BailingMMNativeForConditionalGeneration (Hub `config`), text-to-speech.
- Intended task: Text-to-speech and voice cloning, per the upstream card.
- Role-assigned artifacts: none. The catalog entry is the MLX build below.

## 2. Artifact evidence

### mlx-community/Ming-3.0-tts-0.5B-8bit

- [Artifact metadata](https://huggingface.co/api/models/mlx-community/Ming-3.0-tts-0.5B-8bit?blobs=true),
  observed 2026-11-22; artifact repository created 2026-10-19.
- Artifact repository: `mlx-community/Ming-3.0-tts-0.5B-8bit`.
- Artifact publisher: `mlx-community` (`author`).
- Immutable artifact revision: `d0d1da6f627e4b3f20cc2db6ba4aee86d45343ad` (`sha`).
- Artifact created date: 2026-10-19T17:00:55.000Z (`createdAt`).
- Evidence observed date: 2026-11-22,
  [Hub API](https://huggingface.co/api/models/mlx-community/Ming-3.0-tts-0.5B-8bit?blobs=true).
- Quantization recipe: affine 8-bit, group size 64,
  [pinned config](https://huggingface.co/mlx-community/Ming-3.0-tts-0.5B-8bit/blob/d0d1da6f627e4b3f20cc2db6ba4aee86d45343ad/config.json),
  observed 2026-11-22.
- Calibration provenance: not applicable; MLX affine 8-bit quantization in
  the pinned config applies no calibration data,
  [pinned config](https://huggingface.co/mlx-community/Ming-3.0-tts-0.5B-8bit/blob/d0d1da6f627e4b3f20cc2db6ba4aee86d45343ad/config.json),
  observed 2026-11-22.
- Upstream source revision: not published by converter; the artifact card
  declares no `base_model`.
- Weight files: UNVERIFIED (not enumerated for this revision).
- Maximum positions in the pinned config: 32768 (`llm_config.max_position_embeddings`).
  The catalog serves 32768.

### audio-cpp/Ming-3.0-TTS-0.5B-GGUF

- Artifact metadata: [Hugging Face API](https://huggingface.co/api/models/audio-cpp/Ming-3.0-TTS-0.5B-GGUF?blobs=true),
  observed 2026-11-22.
- Artifact repository: `audio-cpp/Ming-3.0-TTS-0.5B-GGUF`.
- Artifact publisher: `audio-cpp` (`author`).
- Immutable artifact revision: `2eb8d37c7f10672e69c8aa33091baa04c461b66c` (`sha`).
  [Pinned file](https://huggingface.co/audio-cpp/Ming-3.0-TTS-0.5B-GGUF/blob/2eb8d37c7f10672e69c8aa33091baa04c461b66c/ming-3.0-tts-0.5b-q8_0.gguf).
- Artifact created date: 2026-10-21T03:55:46.000Z (`createdAt`), per the Hub API.
- Evidence observed date: 2026-11-22,
  [Hub API](https://huggingface.co/api/models/audio-cpp/Ming-3.0-TTS-0.5B-GGUF?blobs=true).
- Filename and bytes: `ming-3.0-tts-0.5b-q8_0.gguf`, 1742280896 bytes.
  SHA256: `fcf2aa25e8e9cf2065a936e506581735c64d6255fb7869f09fbb61a2dde09aa1`,
  from `siblings[].lfs.sha256` at the pinned artifact revision.
- Quantization recipe: GGUF `Q8_0`, identified by the published artifact filename;
  [audio.cpp Ming TTS model guide](https://github.com/0xShug0/audio.cpp/blob/04a37f2e/docs/models/ming3_tts.md).
- Calibration provenance: not applicable; Q8_0 GGUF block quantization, with no calibration dataset listed in the artifact metadata or model guide.
- Transformation: audio-cpp publishes a Q8_0 GGUF conversion of the upstream Ming checkpoint; the GGUF includes the backbone, flow head, VAE and speaker encoder per the pinned model guide.

## 3. Runtime and memory

- Runtime: `mlx-audio` 0.6.5 serves model_type `dense` (`tts/models/dense`) through
  `POST /v1/audio/speech`. Ming-3.0 is detected by the dense model class's README.
  Runtime qualification on this host: UNVERIFIED (no model runs yet).
- Memory budget: UNVERIFIED.

## 4. Evaluation and comparison

- Benchmark: Seed-TTS testset zero-shot WER (seed-tts-eval-zh),
  Ming-3.0-tts-0.5b row of the upstream card; score: 0.800; date: 2026-11-22;
  source: <https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B/blob/ffd36ab5764c39c7e5565dfed66a3aeeced58ab9/README.md>

## 5. Trial status

- Dated promotion decision: UNVERIFIED (no trial run).
- Predeclared acceptance criteria: UNVERIFIED.
- Unresolved fields: runtime qualification, memory budget, task-matched
  comparison, and trial evidence.
