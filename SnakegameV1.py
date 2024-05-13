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

keys_down = {}
assets = {} #dicionario de imagens e sons
assets['fundo'] =  pygame.image.load('campo.png').convert()
assets['fundo'] = pygame.transform.scale(assets['fundo'], (WIDTH,HEIGHT))
assets['cobra'] = pygame.image.load('OIG1.jpg').convert()
assets['cobra']= pygame.transform.scale(assets['cobra'], (40,40))
assets['apple'] = pygame.image.load('lixo.png').convert()
assets['apple']= pygame.transform.scale(assets['apple'],(tmnh_bloco_map,tmnh_bloco_map))
assets['maracana'] = pygame.image.load('maracana.jpg').convert()
assets['maracana'] = pygame.transform.scale(assets['maracana'],(WIDTH,HEIGHT))
assets['FLA'] = pygame.transform.scale(assets['apple'],(tmnh_bloco_map*4, tmnh_bloco_map*4))
assets['FLU'] = pygame.image.load('Fluminense_FC_escudo.png').convert()
assets['FLU'] = pygame.transform.scale(assets['FLU'],(tmnh_bloco_map*4, tmnh_bloco_map*4))
assets['som'] = pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')


#Criando cobra

class Snake(pygame.sprite.Sprite):

    def _init_(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite._init_(self)

        self.x, self.y = tmnh_bloco_map, tmnh_bloco_map
        self.xdir = 1
        self.ydir = 0
        self.image = assets['cobra']  # Directly assign the image from assets
        self.rect = self.image.get_rect()
        self.body = [pygame.Rect(self.x, self.y, tmnh_bloco_map, tmnh_bloco_map)]
        self.head = pygame.Rect(self.x - tmnh_bloco_map, self.y, tmnh_bloco_map, tmnh_bloco_map)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        self.body.append(self.head)  # Adding the head to the body
        for i in range(len(self.body) - 1):  # for each block of the body, move one step ahead relative to its previous
            self.body[i].x = self.body[i + 1].x
            self.body[i].y = self.body[i + 1].y
        self.head.x += self.xdir * tmnh_bloco_map  # moving the head 1 square
        self.head.y += self.ydir * tmnh_bloco_map
        self.body.remove(self.head)