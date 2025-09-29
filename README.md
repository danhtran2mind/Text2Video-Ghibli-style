# Text to Video Ghibli style 🎞️ (Text2Video-Ghibli-style)

[![GitHub Stars](https://img.shields.io/github/stars/danhtran2mind/Text2Video-Ghibli-style?style=social&label=Repo%20Stars)](https://github.com/danhtran2mind/Text2Video-Ghibli-style/stargazers)
![Badge](https://hitscounter.dev/api/hit?url=https%3A%2F%2Fgithub.com%2Fdanhtran2mind%2FText2Video-Ghibli-style&label=Repo+Views&icon=github&color=%236f42c1&message=&style=social&tz=UTC)

[![huggingface-hub](https://img.shields.io/badge/huggingface--hub-blue.svg?logo=huggingface)](https://huggingface.co/docs/hub)
[![accelerate](https://img.shields.io/badge/accelerate-blue.svg?logo=pytorch)](https://huggingface.co/docs/accelerate)
[![torch](https://img.shields.io/badge/torch-blue.svg?logo=pytorch)](https://pytorch.org/)
[![transformers](https://img.shields.io/badge/transformers-blue.svg?logo=huggingface)](https://huggingface.co/docs/transformers)
[![torchvision](https://img.shields.io/badge/torchvision-blue.svg?logo=pytorch)](https://pytorch.org/vision/stable/index.html)
[![diffusers](https://img.shields.io/badge/diffusers-blue.svg?logo=huggingface)](https://huggingface.co/docs/diffusers)
[![gradio](https://img.shields.io/badge/gradio-blue.svg?logo=gradio)](https://gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Introduction
Transform text into captivating videos with the enchanting aesthetic of Studio Ghibli. This project leverages a fine-tuned `zeroscope_v2_576w` model to generate high-quality, Ghibli-inspired video content from text prompts. Built upon the foundation of [MotionDirector](https://github.com/showlab/MotionDirector), it includes optimized code and enhanced stability for seamless performance. 🌟

## Key Features
- 🎨 Generate videos in the iconic Studio Ghibli art style
- ⚡ Optimized for efficiency with fine-tuned zeroscope_v2_576w
- 🛠️ User-friendly notebooks for training and inference
- 🌐 Interactive Gradio demo for real-time video generation
- 🔧 Enhanced stability and performance over the original MotionDirector

## Notebook
Explore the project with our comprehensive notebook: 
### Training Notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb)
[![Open in SageMaker](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb)
[![Open in Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?url=https://github.com/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb)
[![JupyterLab](https://img.shields.io/badge/Launch-JupyterLab-orange?logo=Jupyter)](https://mybinder.org/v2/gh/danhtran2mind/Text2Video-Ghibli-style/main?filepath=notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb)
[![Open in Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb)
[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/danhtran2mind/Text2Video-Ghibli-style/main)
[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb)
[![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Fdanhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Training.ipynb)

### Inference Notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb)
[![Open in SageMaker](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb)
[![Open in Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?url=https://github.com/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb)
[![JupyterLab](https://img.shields.io/badge/Launch-JupyterLab-orange?logo=Jupyter)](https://mybinder.org/v2/gh/danhtran2mind/Text2Video-Ghibli-style/main?filepath=notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb)
[![Open in Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb)
[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/danhtran2mind/Text2Video-Ghibli-style/main)
[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/danhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb)
[![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Fdanhtran2mind/Text2Video-Ghibli-style/blob/main/notebooks/zeroscope_v2_576w_Ghibli_LoRA-Inference.ipynb)


## Dataset
You can explore more in this HuggingFace Dataset available at the given link for further details: [![HuggingFace Dataset](https://img.shields.io/badge/HuggingFace-raymondt%2Fghibi__t2v-yellow?style=flat&logo=huggingface)](https://huggingface.co/datasets/raymondt/ghibi_t2v).

The model is trained on a curated dataset inspired by Studio Ghibli's visual style, ensuring authentic and high-quality video outputs. Details are available in the [dataset processing script](scripts/process_dataset.py). 📊

## Base Model
This project builds upon the `zeroscope_v2_576w` model, fine-tuned with LoRA for Ghibli-style video generation, forked from [MotionDirector](https://github.com/showlab/MotionDirector). 🚀

## Demonstration
Experience the magic of Ghibli-style video generation:  
- **HuggingFace Space**: [![HuggingFace Space Demo](https://img.shields.io/badge/HuggingFace-danhtran2mind%2FText2Video--Ghibli--style-yellow?style=flat&logo=huggingface)](https://huggingface.co/spaces/danhtran2mind/Text2Video-Ghibli-style)

- **Demo GUI**:  
  <img src="./assets/gradio_app_demo.jpg" alt="Gradio Demo" height="600">

To run the Gradio app locally (`localhost:7860`):  
```bash
python apps/gradio_app.py
```

## Usage Guide

### Setup Instructions

#### Step 1: Clone the Repository
Clone the project repository and navigate to the project directory:
```bash
git clone https://github.com/danhtran2mind/Text2Video-Ghibli-style.git
cd Text2Video-Ghibli-style
```

#### Step 2: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements/requirements.txt
```

#### Step 3: Configure the Environment
Run the following scripts to set up the project:
- **Install Third-Party Dependencies**  
  ```bash
  python scripts/setup_third_party.py
  ```
- **Download Model Checkpoints**  
  ```bash
  python scripts/download_ckpts.py
  ```
- **Prepare Dataset (Optional, for Training)**  
  ```bash
  python scripts/process_dataset.py
  ```

### Training
- To train the model:
```bash
python src/text2video_ghibli_style/train.py
```
- Training Hyperparameters
Refer to the [Training Documents](docs/training/training_doc.md) for detailed hyperparameters used in fine-tuning the model. ⚙️

### Inference
To generate videos using the trained model:
```bash
python src/text2video_ghibli_style/inference.py
```

## Inference Samples

<table>
  <thead>
    <tr>
      <th>Prompt</th>
      <th>Video</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">A dog is running with Ghibli style</td>
      <td style="text-align: center;"><img src="assets/examples/zeroscope_v2_576w-Ghibli-LoRA/1/A_dog_is_running_with_Ghibli_style_42.gif" alt="Example 1 gif"></td>
    </tr>
    <tr>
      <td style="text-align: center;">A girl is walking with Ghibli style</td>
      <td style="text-align: center;"><img src="assets/examples/zeroscope_v2_576w-Ghibli-LoRA/2/A_girl_is_walking_with_Ghibli_style_0.gif" alt="Example 2 gif"></td>
    </tr>
    <tr>
      <td style="text-align: center;">Studio Ghibli style. Young man contemplates, walks away from ivy-covered yellow building.</td>
      <td style="text-align: center;"><img src="assets/examples/zeroscope_v2_576w-Ghibli-LoRA/3/Studio_Ghibli_style_Young_man_contemplates_walks_away_from_ivy-covered_yellow_building_12345.gif" alt="Example 3 gif"></td>
    </tr>
    <tr>
      <td style="text-align: center;">Studio Ghibli style. Two women walk down coastal village path toward sea, passing colorful houses, sailboats visible.</td>
      <td style="text-align: center;"><img src="assets/examples/zeroscope_v2_576w-Ghibli-LoRA/4/Studio_Ghibli_style_Two_women_walk_down_coastal_village_path_toward_sea_passing_colorful_houses_sailboats_visible_100.gif" alt="Example 4 gif"></td>
    </tr>
  </tbody>
</table>

## Environment
- **Python**: 3.10 or higher
- **Key Libraries**: See [requirements_compatible.txt](requirements/requirements_compatible.txt) for compatible versions
<!-- 
## Contact
For questions or issues, please use the [GitHub Issues tab](https://github.com/danhtran2mind/Text2Video-Ghibli-style/issues) or the [Hugging Face Community tab](https://huggingface.co/spaces/danhtran2mind/Text2Video-Ghibli-style/discussions). 📬 -->

## Project Description

This repository is trained from [![GitHub Repo](https://img.shields.io/badge/GitHub-danhtran2mind%2FMotionDirector-blue?style=flat&logo=github)](https://github.com/danhtran2mind/MotionDirector), a fork of [![GitHub Repo](https://img.shields.io/badge/GitHub-showlab%2FMotionDirector-blue?style=flat&logo=github)](https://github.com/showlab/MotionDirector), with numerous bug fixes and rewritten code for improved performance and stability. You can download the `zeroscope_v2_576w` model from the [![HuggingFace: cerspense/zeroscope_v2_576w](https://img.shields.io/badge/HuggingFace-cerspense%2Fzeroscope__v2__576w-yellow?logo=huggingface)](https://huggingface.co/cerspense/zeroscope_v2_576w). Explore more models on [![HuggingFace Hub](https://img.shields.io/badge/HuggingFace-cerspense-yellow?style=flat&logo=huggingface)](https://huggingface.co/cerspense).
