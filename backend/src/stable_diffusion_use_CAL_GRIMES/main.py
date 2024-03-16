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
async def predict(prompt: str):
    stable_diffusion = StableDiffusion()
    stable_diffusion(prompt) if prompt != '' else stable_diffusion()
    return {"message": "Prediction made successfully!"}