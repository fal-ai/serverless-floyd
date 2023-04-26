from fal_serverless import isolated

requirements = [
    "deepfloyd_if==1.0.0",
    "xformers==0.0.16",
    "git+https://github.com/openai/CLIP.git"
]

@isolated(requirements=requirements)
def test():
    