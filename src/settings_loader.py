import yaml
from src.question import Question

with open("settings.yml") as f:
    data = yaml.safe_load(f)

questions = [Question(**q) for q in data["Questions"]]