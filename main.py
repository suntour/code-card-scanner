import config
import loader
import scanner

image_folder = config.get_folder()

cards = loader.load_cards_from_folder(image_folder)

if cards:
    scanner.scan(cards)
