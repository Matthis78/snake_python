import pygame
import random
from display import *
from colors import *

def the_snake(snake_size, snake_tab):
    for x in snake_tab:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_size, snake_size])


def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 5, dis_height / 2])

def messagePause(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 2, dis_height / 2])

def pause():
    game_over = False
    image = pygame.image.load("snake-game.jpg")
    dis.blit(image, (0, 0))
    messagePause("Pause", white)
    pause_font = pygame.font.SysFont("roboto", 40)
    loop = 1
    pause_font.render("PAUSED", 500, 150)
    pause_font.render("Press Space to continue", 500, 250)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    dis.fill((0,0,0))
                    loop = 0
        pygame.display.update()
