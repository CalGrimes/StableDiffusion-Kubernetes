from model.stable_diffusion import StableDiffusion

def main():
    # prompt input
    prompt = input("Enter a prompt: ")

    # call the model
    stable_diffusion = StableDiffusion()
    stable_diffusion() if prompt == '' else stable_diffusion(prompt)


if __name__ == "__main__":
    main()
