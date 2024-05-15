import pygame
import random

WIDTH = 760
HEIGHT = 680
tmnh_bloco_map = 40

window = pygame.display.set_mode((WIDTH, HEIGHT))
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


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.x, self.y = tmnh_bloco_map, tmnh_bloco_map
        self.xdir = 1
        self.ydir = 0
        self.image = assets['cobra']  
        self.rect = self.image.get_rect()
        self.body = [pygame.Rect(self.x, self.y, tmnh_bloco_map, tmnh_bloco_map)]
        self.head = pygame.Rect(self.x - tmnh_bloco_map, self.y, tmnh_bloco_map, tmnh_bloco_map)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        self.body.append(self.head)  # Adicionando a cabeça ao corpo
        for i in range(len(self.body) - 1): #para cada bloco do corpo, mova uma posição à frente relativa a sua ultima
            self.body[i].x = self.body[i + 1].x
            self.body[i].y = self.body[i + 1].y
        self.head.x += self.xdir * tmnh_bloco_map  # mover a cabeça em 1 quadrado
        self.head.y += self.ydir * tmnh_bloco_map
        self.body.remove(self.head)
     

class Apple:
    def __init__(self):
        self.x = int(random.randint (0,WIDTH)/tmnh_bloco_map)*tmnh_bloco_map
        self.y = int(random.randint(0,HEIGHT)/tmnh_bloco_map)*tmnh_bloco_map
        self.image = assets['apple']  
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.x,self.y,tmnh_bloco_map,tmnh_bloco_map)
    def update(self):
        window.blit(assets['apple'], self.rect)