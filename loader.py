import os
import cv2

class CardCodeObject:
    def __init__(self, image, image_name):
        self.image = image
        self.name = image_name
    
    def __str__(self):
        return self.name
    
    def get_image(self):
        return self.image

def load_cards_from_folder(folder):
    cards = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            cards.append(CardCodeObject(img, filename))
    return cards