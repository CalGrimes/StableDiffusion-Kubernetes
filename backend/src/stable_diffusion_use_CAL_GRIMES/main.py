from fastapi import FastAPI, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from model.stable_diffusion import StableDiffusion
import time

app = FastAPI()

origins = [
    "http://localhost/3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(prompt: str):
    def generate():
        stable_diffusion = StableDiffusion()
        for i in range(100):
            # Simulate a long-running task
            time.sleep(0.1)
            stable_diffusion(prompt) if prompt != '' else stable_diffusion()
            yield f"data: {i+1}\n\n"  # Send progress to the client

    return StreamingResponse(generate(), media_type="text/event-stream")