from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'foto.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

pil_image = Image.open(IMAGE_PATH)
width,height = pil_image.size
# exif = pil_image.info['exif']

new_width = 640
new_hight = round(height * new_width / width)

new_size = pil_image.resize((new_hight, new_width))
new_size.save(
    NEW_IMAGE,
    optimize=True,
)