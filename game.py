import pygame
import time
import random


pygame.init()

from Gamefunction import *
from display import *
from colors import *
from score import *
import os

clock = pygame.time.Clock()

snake_size = 10
snake_vit = 20


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_tab = []
    Length_of_snake = 1

    itemx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
    itemy = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("Appuyez sur O pour lire ou N pour quitter", white)
            score(Length_of_snake - 1)
            pygame.display.update()



            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_o:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
                elif event.key == pygame.K_SPACE:
                                pause()


        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [itemx, itemy, snake_size, snake_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_tab.append(snake_Head)
        if len(snake_tab) > Length_of_snake:
            del snake_tab[0]

        for x in snake_tab[:-1]:
            if x == snake_Head:
                game_close = True

        the_snake(snake_size, snake_tab)

        score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == itemx and y1 == itemy:
            itemx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
            itemy = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1


        clock.tick(snake_vit)

    pygame.quit()
    quit()


gameLoop()