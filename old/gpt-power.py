import requests
import os
HF_API_KEY= os.getenv("HUGGING_FACE_TOKEN")

headers = {"Authorization": f"Bearer {HF_API_KEY}"}
data = {
    "inputs": ' ""Write a Python script that opens a specific folder and prints all the file names inside it. Use the `os` module."'
}

response = requests.post(
    "https://api-inference.huggingface.co/models/bigcode/starcoder",
    headers=headers,
    json=data
)

print(response.json())  # Generated code
