from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipeline.to("cuda")

prompt = "An image of an astronaut riding a horse"

image = pipeline(prompt).images[0]

image.save("output/astronaut_horse.png")
