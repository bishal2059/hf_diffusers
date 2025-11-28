# HuggingFace Diffusers Project

A simple implementation using HuggingFace Diffusers library to generate images with Stable Diffusion.

## Setup

### Create Conda Environment

```bash
conda create -n diffusers python=3.9
conda activate diffusers
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install PyTorch with CUDA Support (if using GPU)

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

## Usage

Run the image generation script:

```bash
python stable_diffuser.py
```

The generated image will be saved in the `output/` directory.

## Output

Generated images are saved to the `output/` folder as PNG files.