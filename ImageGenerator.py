import os
from pathlib import Path
import openai
import json
from base64 import b64decode

openai.api_key = "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"

# generate image
PROMPT = "nuclear aftermath"
DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)


# decode image
DATA_DIR = Path.cwd() / "responses"
JSON_FILE = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"
IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)

file_name = f"{PROMPT[:5]}-{response['created']}.json"

os.remove("responses/" + file_name)