from PIL import Image, ImageEnhance
import os

input_path = "average_state_flag/AverageImage.png"
output_path = "enhanced_state_flag/AverageImage.png"

image = Image.open(input_path)
enhancer = ImageEnhance.Contrast(image)
factor = 2
enhanced_image = enhancer.enhance(factor)

enhanced_image.save(output_path)
