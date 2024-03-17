from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from polling.task import Task
import torch

class StableDiffusion:
    def __init__(self):
        self.model_id = "stabilityai/stable-diffusion-2-1"
        self.tasks = {}  # Add a tasks dictionary to the StableDiffusion class

    def callback_dynamic_cfg(self, task, pipe, step_index, timestep,  *args, **callback_kwargs):
        # adjust the batch_size of prompt_embeds according to guidance_scale
        if step_index == int(pipe.num_timesteps * 0.4):
                prompt_embeds = callback_kwargs["prompt_embeds"]
                prompt_embeds = prompt_embeds.chunk(2)[-1]

                # update guidance_scale and prompt_embeds
                pipe._guidance_scale = 0.0
                callback_kwargs["prompt_embeds"] = prompt_embeds

        # update task status and percentage
        task.set_task(task.task_id, 'in_progress', int((step_index / pipe.num_timesteps) * 100))

        return callback_kwargs

    def predict(self, prompt="a photo of an astronaut riding a horse on mars", task=None):
        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float32)
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe = pipe.to("cuda")

        generator = torch.Generator(device="cuda").manual_seed(1)
        out = pipe(
            prompt,
            generator=generator,
            callback_on_step_end=lambda *args, **kwargs: self.callback_dynamic_cfg(task, *args, **kwargs),
            callback_on_step_end_tensor_inputs=['prompt_embeds']
        )
        # Update the task status to 'completed' after the image is saved
        task.set_task(task.task_id, 'complete', 100)

        out.images[0].save(prompt.replace(" ", "_") + ".png")
        return out.images[0]

    def __call__(self, prompt="a photo of an astronaut riding a horse on mars"):
        prompt = prompt.replace("%20", " ")

        # Create an instance of Task
        task = Task(task_id=prompt, status="started")

        # Call the predict method with the prompt and task_id
        self.predict(prompt=prompt, task=task)

        


    