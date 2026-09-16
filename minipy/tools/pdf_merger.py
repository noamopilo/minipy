import PyPDF2
import sys
import os
import shutil
from pathlib import Path

downloads_path = Path.home() / "Downloads"
folder_path = downloads_path / "minipy_PDFS"

if not folder_path.exists():
    folder_path.mkdir(parents=True, exist_ok=True)
    

merger = PyPDF2.PdfMerger()
pdf = "no"

print(f"Put the pdfs that you want merged in the /minipy_PDFS folder in your Downloads (this is a temporary folder and will be deleted after merging)\n")
input("Press enter when done...")

while pdf == "no":
    filename = input("What should be the name of the merged pdf? (with .pdf): ")
    
    if not filename.endswith(".pdf"):
        print("The file name must end with .pdf")
    else:
        pdf ="yes"

pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

if not pdf_files:
    print("No PDF files found, merging cancceled..")
    shutil.rmtree(folder_path)
    sys.exit()

try:
    for file in sorted(pdf_files):
        print(f"Merging {file}...")
        full_path = os.path.join(folder_path, file)
        merger.append(full_path)
            
    output_path = downloads_path / filename
    merger.write(str(output_path))
    merger.close()

    shutil.rmtree(folder_path)
finally:
    shutil.rmtree(folder_path)