# text-to-video-genshin-style

[![GitHub Stars](https://img.shields.io/github/stars/danhtran2mind/Text2Video-Ghibli-style?style=social&label=Repo%20Stars)](https://github.com/danhtran2mind/Text2Video-Ghibli-style/stargazers)
![Badge](https://hitscounter.dev/api/hit?url=https%3A%2F%2Fgithub.com%2Fdanhtran2mind%2FText2Video-Ghibli-style&label=Repo+Views&icon=github&color=%236f42c1&message=&style=social&tz=UTC)



## Introduction

## Key Features
## Notebooks
- Training: ./notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb
- Inference: ./notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb

## Installation
```bash
git clone https://github.com/danhtran2mind/Text2Video-Ghibli-style
```
```bash
cd Text2Video-Ghibli-style
```
```bash
pip install -r requirements/requirements.txt
```

```bash
python scripts/setup_third_party.py
```

```bash
python scripts/download_ckpts.py
```

```bash
python scripts/process_dataset.py
```

## Usage
### Training
```python
python src/text2video_ghibli_style/train.py
```

### Inference
```python
python src/text2video_ghibli_style/inference.py
```

## Demonstration
### Interactive Demo
https://huggingface.co/spaces/danhtran2mind/Text2Video-Ghibli-style

Below is a screenshot of the SlimFace Demo GUI:

<img src="./assets/gradio_app_demo.jpg" alt="SlimFace Demo" height="600">

### Run Locally

To run the Gradio application locally at the default address `localhost:7860`, execute:

```bash
python apps/gradio_app.py
```

## Environment

SlimFace requires the following environment:

- **Python**: 3.10 or higher
- **Key Libraries**: Refer to [Requirements Compatible](./requirements/requirements_compatible.txt) for compatible dependencies.


## Project Description

This repository is trained from [![GitHub Repo](https://img.shields.io/badge/GitHub-danhtran2mind%2FMotionDirector-blue?style=flat)](https://github.com/danhtran2mind/MotionDirector), a fork of [![GitHub Repo](https://img.shields.io/badge/GitHub-showlab%2FMotionDirector-blue?style=flat)](https://github.com/showlab/MotionDirector), with numerous bug fixes and rewritten code for improved performance and stability. You can explore more model in HuggingFace Hub https://huggingface.co/cerspense.