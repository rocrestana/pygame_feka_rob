import pygame
import random

pygame.init()
pygame.mixer.init()

# Dimensões:
WIDTH = 760
HEIGHT = 680
tmnh_bloco_map = 40

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
tempo = pygame.time.Clock()