import os
import json

folder="img"
base_url = "https://cdn.jsdelivr.net/gh/kerwin1950/photo-gallery@main"

files=os.listdir(folder)
image_urls = [f"{base_url}/{folder}/{file}" for file in files if file.endswith(('.jpg', '.png', '.jpeg', '.gif'))]

data = {"images": image_urls}

with open("images.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4)

print("已生成images.json!")