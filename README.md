# code-card-scanner
This program uses [tesseract-ocr](https://github.com/tesseract-ocr/tesseract) to scan a folder of code card images.

The output is a text file with the extracted codes, as well as the names of the images that failed to scan.

# Setup
In config.py:
Change `tesseract_path` to point to your tesseract installation.

Change `image_folder` to point to your folder of images to scan.

# How to run
Run `python main.py`
