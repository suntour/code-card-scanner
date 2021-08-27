image_folder = r"C:\Users\USER_NAME\Desktop\test_folder"

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pattern = "[a-zA-Z0-9]{3}[-][a-zA-Z0-9]{4}[-][a-zA-Z0-9]{3}[-][a-zA-Z0-9]{3}"
output_file_name = r"output.txt"

def get_folder():
    return image_folder

def get_tesseract_path():
    return tesseract_path

def get_pattern():
    return pattern

def get_output_file_name():
    return output_file_name