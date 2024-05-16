import pygame
import random
import os
from classes import *
from assets import *


WIDTH = 760
HEIGHT = 680
tmnh_bloco_map = 40

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
tempo = pygame.time.Clock()
font = pygame.font.Font("font.ttf", tmnh_bloco_map*2)
font2 = pygame.font.Font("font.ttf", 60)
font3 = pygame.font.Font("font.ttf", tmnh_bloco_map*3)
font4 = pygame.font.Font("font.ttf", tmnh_bloco_map)