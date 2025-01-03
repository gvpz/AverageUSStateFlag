from PIL import Image, ImageOps
import os

import_path = "pictures"
export_path = "resized_pictures"

target_size = (2560, 2250)


def resize_with_padding(image_path, target_size):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    image = ImageOps.pad(image, target_size, method=Image.Resampling.LANCZOS, color=(0, 0, 0, 0))
    return image

for filename in os.listdir(import_path):
    if filename.lower().endswith(".png"):
        image_path = os.path.join(import_path, filename)
        save_path = os.path.join(export_path, filename)
        resized_image = resize_with_padding(image_path, target_size)
        resized_image.save(save_path)
