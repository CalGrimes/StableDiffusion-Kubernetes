from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from polling.task import Task
import torch

class StableDiffusion:
    def __init__(self):
        self.model_id = "stabilityai/stable-diffusion-2-1"
        self.tasks = {}  # Add a tasks dictionary to the StableDiffusion class

    def callback_dynamic_cfg(self, task_id, pipe, step_index, timestep,  *args, **callback_kwargs):
        # adjust the batch_size of prompt_embeds according to guidance_scale
        if step_index == int(pipe.num_timesteps * 0.4):
                prompt_embeds = callback_kwargs["prompt_embeds"]
                prompt_embeds = prompt_embeds.chunk(2)[-1]

                # update guidance_scale and prompt_embeds
                pipe._guidance_scale = 0.0
                callback_kwargs["prompt_embeds"] = prompt_embeds

        # update task status and percentage
        new_task = self.tasks[task_id]
        new_task.update_task_status(task_id, 'in_progress')
        new_task.percent_complete = int((step_index / pipe.num_timesteps) * 100)

        new_task(task_id, 'in_progress', new_task.percent_complete)
        return callback_kwargs

    def predict(self, prompt="a photo of an astronaut riding a horse on mars", task_id=""):
        new_task = self.tasks[task_id]


        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float32)
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe = pipe.to("cuda")

        generator = torch.Generator(device="cuda").manual_seed(1)
        out = pipe(
            prompt,
            generator=generator,
            callback_on_step_end=lambda *args, **kwargs: self.callback_dynamic_cfg(task_id, *args, **kwargs),
            callback_on_step_end_tensor_inputs=['prompt_embeds']
        )
        # Update the task status to 'completed' after the image is saved
        Task(task_id=task_id, status='in_progress', percent_complete=100)
        out.images[0].save(prompt.replace(" ", "_") + ".png")

    def __call__(self, prompt="a photo of an astronaut riding a horse on mars"):
        prompt = prompt.replace("%20", " ")

        # Create a new task with status 'pending'
        task_id = prompt.replace(" ", "_")
        new_task = Task(task_id=task_id, status='in_progress')
        new_task(task_id, 'pending', 0)
        self.tasks[new_task.task_id] = new_task

        # Call the predict method with the prompt and task_id
        self.predict(prompt, task_id)

        


    