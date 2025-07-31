# Training Hyperparameters Document

Below is a table summarizing the configuration parameters for training a video generation model with a pretrained diffusers model, configured for Studio Ghibli-style LoRA training.

| Parameter | Value | Description |
|-----------|-------|-------------|
| **Pretrained Model Path** | `./ckpts/zeroscope_v2_576w` | Path to the pretrained Zeroscope V2 576w model. |
| **Output Directory** | `./zeroscope_v2_576w-Ghibli-LoRA` | Directory for saving training outputs (checkpoints, logs). |
| **Dataset Types** | `folder` | Dataset loaded from a folder of video files. |
| **Cache Latents** | `True` | Caches latents to disk to save memory and speed up training. |
| **Cached Latent Directory** | `null` | Path to pre-cached latents (skips caching if specified). |
| **Use UNET LoRA** | `True` | Enables LoRA for the UNET model to reduce memory usage. |
| **LoRA UNET Dropout** | `0.1` | Dropout probability for LoRA layers to prevent overfitting. |
| **LoRA Rank** | `16` | Rank for LoRA training, balancing VRAM and capacity. |
| **Save Pretrained Model** | `True` | Saves full pretrained model weights for checkpoints. |
| **Train Data: Path** | `./data/ghibli/videos` | Directory containing training videos. |
| **Train Data: Width** | `384` | Target width for resizing training videos. |
| **Train Data: Height** | `384` | Target height for resizing training videos. |
| **Train Data: Use Bucketing** | `True` | Adjusts resolution to closest aspect ratio. |
| **Train Data: Gradient Accumulation Steps** | `2` | Steps to accumulate gradients before weight update. |
| **Train Data: Batch Size** | `1` | Number of samples per batch. |
| **Train Data: Sample Start Index** | `1` | Starting frame index for video sampling. |
| **Train Data: FPS** | `16` | Frame sampling rate for folder dataset. |
| **Train Data: Frame Step** | `1` | Step size for frame sampling (e.g., every frame). |
| **Train Data: Number of Sample Frames** | `24` | Number of frames sampled per video. |
| **Validation Data: Prompt** | <ul><li>`Studio Ghibli style. The video showcases a vibrant and lively scene set in the early.`</li><li>`Studio Ghibli style. A woman with black hair is holding a gun in her hand.`</li></ul> | Custom prompts for validation. |
| **Validation Data: Sample Preview** | `False` | Disables preview sampling during training. |
| **Validation Data: Number of Frames** | `24` | Frames to sample during validation. |
| **Validation Data: Width** | `384` | Width of validation samples. |
| **Validation Data: Height** | `384` | Height of validation samples. |
| **Validation Data: Number of Inference Steps** | `15` | Denoising steps during video generation. |
| **Validation Data: Guidance Scale** | `12` | Classifier-free guidance scale. |
| **Validation Data: Spatial Scale** | `0` | Scale for spatial LoRAs. |
| **Validation Data: Noise Prior** | `0` | Scale of inversion noise. |
| **Use Offset Noise** | `False` | Disables offset noise for training. |
| **Offset Noise Strength** | `0.0` | Strength of offset noise (irrelevant if disabled). |
| **Learning Rate** | `5e-4` | Learning rate for AdamW optimizer. |
| **Adam Weight Decay** | `1e-4` | Weight decay for regularization. |
| **Maximum Train Steps** | `5000` | Total training steps before saving model. |
| **Checkpointing Steps** | `5000` | Saves checkpoint every 5000 steps. |
| **Validation Steps** | `5000` | Performs validation every 5000 steps if enabled. |
| **Mixed Precision** | `fp16` | Uses mixed precision training to reduce VRAM. |
| **Gradient Checkpointing** | `True` | Trades speed for lower VRAM usage. |
| **Text Encoder Gradient Checkpointing** | `True` | Gradient checkpointing for text encoder. |
| **Enable XFormers Memory Efficient Attention** | `True` | Uses XFormers for memory-efficient attention. |
| **Use 8-bit Adam** | `True` | Uses 8-bit Adam optimizer to reduce VRAM. |
| **Enable Torch 2 Attention** | `True` | Uses scaled dot-product attention (PyTorch >= 2.0). |

**Notes**:
- Commented parameters (e.g., `resume_step`, `lora_path`) are not active but included in the original configuration for reference.
- The configuration is optimized for memory efficiency and performance, leveraging LoRA, mixed precision, and gradient checkpointing.