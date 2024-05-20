import pygame
import random
import os
from classes import *
from assets import *
from dimensoes import *

def Cria_Mapa():
    for x in range(0, WIDTH, tmnh_bloco_map):
        for y in range(0, HEIGHT, tmnh_bloco_map):
            rect = pygame.Rect(x, y, tmnh_bloco_map, tmnh_bloco_map)
            pygame.draw.rect(window,(255,255,255,0.5), rect, 1)

score = font.render('1',True,"white")
score_rect = score.get_rect(center =(WIDTH/2, HEIGHT/20))
velocidade = font4.render('1',True,"Black")
velo_rect = velocidade.get_rect(center = (1,HEIGHT/20))
Cria_Mapa()