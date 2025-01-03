from PIL import Image
import os

folder_path = "pictures"

max_width = 0
max_height = 0
bigflag = ""

def check_size(image_path):
    with Image.open(image_path) as img:
        return img.size

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png"):
        image_path = os.path.join(folder_path, filename)
        width, height = check_size(image_path)
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height
            bigflag = filename
        
print(f"Width: {max_width} Height: {max_height} BiggestFlag: {bigflag}")