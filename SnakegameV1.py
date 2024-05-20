import pygame
import random
import os
from classes import *
from assets import *
from dimensoes import *
from criacao_de_mapa import *


pygame.init()
pygame.mixer.init()

keys_down = {}

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