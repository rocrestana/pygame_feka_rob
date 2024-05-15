import pygame
import random
import os
import classes

# Dimensões:
WIDTH = 760
HEIGHT = 680
tmnh_bloco_map = 40

keys_down = {}
assets = {}
assets['fundo'] =  pygame.image.load('campo.png').convert()
assets['fundo'] = pygame.transform.scale(assets['fundo'], (WIDTH,HEIGHT))
assets['cobra'] = pygame.image.load('Jogador do Fluzao.webp').convert()
assets['cobra']= pygame.transform.scale(assets['cobra'], (40,40))
assets['apple'] = pygame.image.load('lixo.png').convert()
assets['apple']= pygame.transform.scale(assets['apple'],(tmnh_bloco_map,tmnh_bloco_map))
assets['maracana'] = pygame.image.load('OIG2.jpg').convert()
assets['maracana'] = pygame.transform.scale(assets['maracana'],(WIDTH,HEIGHT))
assets['FLA'] = pygame.transform.scale(assets['apple'],(tmnh_bloco_map*4, tmnh_bloco_map*4))
assets['FLU'] = pygame.image.load('Fluminense_FC_escudo.png').convert()
assets['FLU'] = pygame.transform.scale(assets['FLU'],(tmnh_bloco_map*4, tmnh_bloco_map*4))
assets['som'] = pygame.mixer.music.load("somflu.mp3")