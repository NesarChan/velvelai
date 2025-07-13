import requests
from config import PORNPEN_API_KEY

def generate_nsfw_image(prompt: str):
    resp = requests.post(
        "https://api.pornpen.ai/generate",
        headers={
            "Authorization": f"Bearer {PORNPEN_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "model": "realisticVision",
            "quality": "hd"
        }
    )
    if resp.ok:
        data = resp.json()
        return data.get("image_url"), data.get("prompt")
    return None, None
