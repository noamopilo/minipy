import os
os.environ["OMP_NUM_THREADS"] = "2"

from rembg import remove, new_session
from PIL import Image
import io
from pathlib import Path
import shutil
import sys

downloads_path = Path.home() / "Downloads"
folder_path = downloads_path / "minipy_images(remove_bg)"

session = new_session("u2netp")

if not folder_path.exists():
    folder_path.mkdir(parents=True, exist_ok=True)
 
print(f"Put the image(s) that you want the background removed in the /minipy_images(remove_bg) folder in your Downloads (this is a temporary folder and will be deleted after the process).\n")
input("Press Enter when done...")

image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

if not image_files:
    print("No images found in the folder, process canceled...")
    shutil.rmtree(folder_path)
    sys.exit()

try:
    for file in image_files:
        print(f"Removing backgrounf from: {file}...")
        input_path = folder_path / file
        img = Image.open(input_path)
        no_bg_image = remove(img, session=session)
        output_path = folder_path.parent / f"{input_path.stem}_no_bg.png"
        
        no_bg_image.save(output_path)
        print(f"Image saved successfully to {output_path}")

finally:
    shutil.rmtree(folder_path)
    

    