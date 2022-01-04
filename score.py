import pygame
from colors import *
from display import *

score = 0
def score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
