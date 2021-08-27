import os
import config
import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = config.get_tesseract_path()
pattern = config.get_pattern()

def scan(cards):
    codes = []
    failed_scans = []

    for card in cards:
        text = pytesseract.image_to_string(card.get_image())

        extracted_code = re.search(pattern, text)

        if extracted_code:
            codes.append(extracted_code.group())
        else:
            failed_scans.append(str(card))
    
    write_codes(codes, failed_scans)

def write_codes(codes, failed_scans):
    output_file = os.path.join(config.get_folder(), config.get_output_file_name())
    with open(output_file, "w") as f:

        if(codes):
            f.write('Successfully scanned codes:' + '\n')
            for code in codes:
                f.write(''.join(code) + '\n')

        if(failed_scans):
            f.write('\n' + 'Files that failed to scan:' + '\n')
            for fail in failed_scans:
                f.write(''.join(fail) + '\n')



