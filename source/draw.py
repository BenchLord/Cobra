import pygame
import graphics
import game
from sprite import Sprite

def draw():
    """
    Drawing logic
    """

    # Draw background
    game.screen.fill((255, 255, 255))

    # Drawing a sprite called my_sprite
    # my_sprite.draw()

    # Get rid of me!
    game.logo.draw()

    # Draw some text
    # graphics.draw_text("Hello World", (255, 255, 255), (50, 50))

    return