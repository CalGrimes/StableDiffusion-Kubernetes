
# Stable Diffusion Kubernetes Service
🚧 Under construction 🚧
---
## Requirements
A suitable conda environment named ldm can be created and activated with:
```
conda env create -f environment.yaml
conda activate ldm
```

You can also update an existing latent diffusion environment by running
```
conda install pytorch torchvision -c pytorch
pip install transformers==4.19.2 diffusers invisible-watermark
pip install -e .
```
---

Model details can be found on HuggingFace [here](https://huggingface.co/runwayml/stable-diffusion-v1-5).
```
@InProceedings{Rombach_2022_CVPR,
    author    = {Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj\"orn},
    title     = {High-Resolution Image Synthesis With Latent Diffusion Models},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2022},
    pages     = {10684-10695}
}

```


conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
diffusers diffusers-0.27.0
pip install accelerate

conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia