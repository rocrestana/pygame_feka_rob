import pygame
import random
import os

pygame.init()
pygame.mixer.init()

# Dimensões:
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

keys_down = {}
assets = {}
assets['fundo'] =  pygame.image.load('campo.png').convert()
assets['fundo'] = pygame.transform.scale(assets['fundo'], (WIDTH,HEIGHT))
assets['cobra'] = pygame.image.load('Jogador do Fluzao.webp').convert()
assets['cobra']= pygame.transform.scale(assets['cobra'], (40,40))
assets['apple'] = pygame.image.load('Fla.png').convert()
assets['apple']= pygame.transform.scale(assets['apple'],(tmnh_bloco_map,tmnh_bloco_map))
assets['maracana'] = pygame.image.load('OIG2.jpg').convert()
assets['maracana'] = pygame.transform.scale(assets['maracana'],(WIDTH,HEIGHT))
assets['FLA'] = pygame.transform.scale(assets['apple'],(tmnh_bloco_map*4, tmnh_bloco_map*4))
assets['FLU'] = pygame.image.load('Fluminense_FC_escudo.png').convert()
assets['FLU'] = pygame.transform.scale(assets['FLU'],(tmnh_bloco_map*4, tmnh_bloco_map*4))
assets['som'] = pygame.mixer.music.load("somflu.mp3")

#Criando a cobra
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

snake = Snake()
apple = Apple()  # Movido para fora do loop principal
inicio = True
game = False
Fim = False
pygame.mixer.music.play(loops=-1)
while inicio:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            game = True  # Inicia o jogo apenas quando o usuário pressionar uma tecla
            inicio = False  # Sai do loop de tela inicial
            break  # Sai do loop de eventos
    window.fill((0, 0, 0))  # Limpa a tela
    window.blit(assets['maracana'], (0, 0))  # Desenha o fundo da tela inicial
    text = font.render("FLA X FLU/SNAKE GAME", True, "Green")
    text2 = font4.render("APERTE QUALQUER TECLA PARA INICIAR!!!!!", True, "Red")
    window.blit(text, (10, 10))
    window.blit(text2, (10,100))
    pygame.display.flip()  # Atualiza a tela


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            # pygame.quit()
        if game:
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.ydir = 0
                    snake.xdir = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.ydir = 0
                    snake.xdir = 1
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.ydir = -1
                    snake.xdir = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.ydir = 1
                    snake.xdir = 0

    if game:  # Verifica apenas se estivermos jogando
        snake.update()
        for square in snake.body[1:]:  # Começa do segundo elemento para evitar a cabeça
            if snake.head.colliderect(square):  # Verifica se a cabeça colidiu com algum bloco do corpo
                game = False
                Fim = True
                break  # Sai do loop assim que encontrar uma colisão
        if not 0 <= snake.head.x < WIDTH or not 0 <= snake.head.y < HEIGHT:
            game = False  # Se a cabeça sair dos limites do mapa, a cobra morre
            Fim = True
    velocidade = 1
    # Aumenta a velocidade se a pontuação for maior ou igual a 5
    if len(snake.body) + 1 >= 5 and len(snake.body)+1<=9:
        tempo.tick(9)  # Ajusta a velocidade para 15 quadros por segundo
        velocidade+=1
    elif len(snake.body)+1 <5:
        tempo.tick(7)  # Mantém a velocidade padrão
        velocidade = velocidade
    elif len(snake.body)+1 >9 and len(snake.body)+1 <15:
        tempo.tick(11)
        velocidade +=2
    elif len(snake.body)+1 >14:
        tempo.tick(12)
        velocidade+=3

    window.fill((0, 0, 0))  # Limpa a tela
    window.blit(assets['fundo'], (0, 0))  # Desenha o fundo

    # Desenha a cabeça da cobra
    window.blit(assets['cobra'], snake.head)
    window.blit(assets['apple'], apple.rect)
    # Desenha o corpo da cobra
    score = font.render(f'{len(snake.body)+1}', True, 'white')
    velocidade = font4.render(f'VELOCIDADE:{velocidade}', True, 'Black')

    for square in snake.body:
        window.blit(assets['cobra'], square)

    window.blit(score, score_rect)  # Desenha o placar
    window.blit(velocidade,velo_rect ) #Informa a veleocidade
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(snake.head.x, snake.head.y, tmnh_bloco_map, tmnh_bloco_map))
        apple = Apple()

    pygame.display.flip()

# Após a morte da cobra:
while Fim:
    # Jogador derrotado:
    if (len(snake.body) + 1) <= 10:
        window.fill((0, 0, 0))
        txt = font.render("VITÓRIA RUBRO-NEGRA!!", True, "Red")
        txt2 = font2.render("O seu placar final foi de:", True, "white")
        txt3 = font3.render(f'{len(snake.body) + 1}', True, "red")
        window.blit(assets['FLA'], (WIDTH / 2 - 100, 500))
        window.blit(txt, (40, 10))
        window.blit(txt2, (WIDTH / 2 - 275, HEIGHT / 3 - 50))
        window.blit(txt3, (WIDTH / 2 - 50, HEIGHT / 3 + 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()

    # Jogador vencedor:
    elif (len(snake.body) + 1) > 10:
        window.fill((0, 0, 0))
        txt = font.render("VITÓRIA TRICOLOR!!!", True, "Green")
        txt2 = font2.render("O seu placar final foi de:", True, "white")
        txt3 = font2.render(f'{len(snake.body) + 1}', True, "red")
        window.blit(assets['FLU'], (WIDTH / 2 - 100, 500))
        window.blit(txt, (40, 10))
        window.blit(txt2, (WIDTH / 2 - 275, HEIGHT / 3 - 50))
        window.blit(txt3, (WIDTH / 2 - 50, HEIGHT / 3 + 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
    pygame.display.flip()

    Cria_Mapa()

pygame.quit()