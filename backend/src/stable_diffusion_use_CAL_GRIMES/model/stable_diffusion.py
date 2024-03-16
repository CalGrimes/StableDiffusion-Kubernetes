from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

import torch

class StableDiffusion:
    def __init__(self):
        self.model_id = "stabilityai/stable-diffusion-2-1"

    def __call__(self, prompt="a photo of an astronaut riding a horse on mars"):
        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float32)
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        # Check if CUDA is available
        pipe = pipe.to("cuda")

        try:
            image = pipe(prompt).images[0]
            image.save(prompt.replace(" ", "_") + ".png")
        except Exception as e:
            print(f"An error occurred: {e}")