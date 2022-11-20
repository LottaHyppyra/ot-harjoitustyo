import pygame

class Images():

    def __init__(self):
        self.file_names = ["floor", "wall", "player"]

    def download_images(self):
        images = []
        for name in self.file_names:
            images.append(pygame.image.load("src/images/" + name + ".png"))
        return images
