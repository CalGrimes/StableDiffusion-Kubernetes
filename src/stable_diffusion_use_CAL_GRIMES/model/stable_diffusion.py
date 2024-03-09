from diffusers import StableDiffusionPipeline
import torch
class StableDiffusion:
    def __init__(self):
        self.model_id = "runwayml/stable-diffusion-v1-5"


    def __call__(self, prompt="a photo of an astronaut riding a horse on mars"):
        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
        pipe = pipe.to("cuda")

        image = pipe(prompt).images[0]  
            
        image.save(prompt.replace(" ", "_") + ".png")
        