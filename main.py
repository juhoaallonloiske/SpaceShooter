import pygame
import math
import random
from pygame import mixer



# Player
class Player:
    def __init__(self):
        self.img = pygame.image.load('player.png')
        self.x = 370
        self.y = 480
        self.x_change = 0

    def __str__(self):
        return print("Player info: \n" \
                     "Width: {} \n" \
                     "Height: {}".format(self.x, self.y))


def main():
    player1 = Player()
    player1.__str__()

    # Initializing Pygame
    pygame.get_init()
    pygame.font.init()
    pygame.mixer.init()

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    # Background
    background = pygame.image.load('background.png')

main()