import requests
import json
import time
import base64

with open("/home/maha/Projects/Jarvis/backend/tests/image4.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")


url = "http://localhost:8080/v1/chat/completions" 
payload = {
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this image?"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}
            ]
        }
    ],
    "n_predict": 8192,
}



response = requests.post(url, json=payload, stream=True)


