!which convert
from moviepy.config import change_settings

# Set the path to the ImageMagick 'convert' binary explicitly
change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})

!apt-get update && apt-get install -y imagemagick





from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Create a black image
img = Image.new("RGB", (640, 120), color=(0, 0, 0))

# Load font
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 32)  # Available in Colab
except:
    font = ImageFont.load_default()

# Draw text
draw = ImageDraw.Draw(img)
text = "Dandi March 1930 – Salt Satyagraha begins!"

# Get text bounding box for accurate width and height
bbox = font.getbbox(text)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Center position
position = ((640 - text_width) // 2, (120 - text_height) // 2)

# Draw the text on the image
draw.text(position, text, font=font, fill=(255, 255, 255))

# Convert to MoviePy clip
np_img = np.array(img)
image_clip = ImageClip(np_img).set_duration(5)

# Export as video
image_clip.write_videofile("dandi_march_clip.mp4", fps=24)


