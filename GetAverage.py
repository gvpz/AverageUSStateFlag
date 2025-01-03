import numpy as np
from PIL import Image
import os

import_path = "resized_pictures"
export_path = "average_state_flag"

total_array = None

for filename in os.listdir(import_path):
    if filename.lower().endswith(".png"):
        image_path = os.path.join(import_path, filename)
        image = Image.open(image_path)
        image = image.convert("RGBA")
        image_array = np.array(image)

        if total_array is None:
            total_array = np.zeros_like(image_array, dtype=np.float64)
        
        alpha_channel = image_array[:, :, 3] / 255.0
        alpha_channel = alpha_channel[..., np.newaxis]
        total_array[:, :, :3] += image_array[:, :, :3] * alpha_channel
        total_array[:, :, 3] += alpha_channel[:, :, 0]

# Calculate the average
average_array = np.zeros_like(total_array, dtype=np.uint8)
average_array[:, :, :3] = (total_array[:, :, :3] / total_array[:, :, 3, np.newaxis])
average_array[:, :, 3] = (total_array[:, :, 3] / len(os.listdir(import_path))) * 255

average_image = Image.fromarray(average_array.astype(np.uint8))

save_path = os.path.join(export_path, "AverageImage.png")
average_image.save(save_path)
