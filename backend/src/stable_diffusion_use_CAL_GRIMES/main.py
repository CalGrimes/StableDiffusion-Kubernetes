from model.stable_diffusion import StableDiffusion
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
async def predict(prompt: str) -> dict:
    stable_diffusion = StableDiffusion()
    image = stable_diffusion(prompt) if prompt != '' else stable_diffusion()
    return {"image": image}



