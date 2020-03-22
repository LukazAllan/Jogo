# Author: Allan Lucas
#

import pygame
from sys import exit
from json import load
from random import randint as rd

# Carregando Dados
with open('data/data.json', 'r', encoding='utf-8') as raw:
    data = load(raw)

# Preparando a Janela
pygame.init() #inicia o pygame
clock = pygame.time.Clock()
ecra_largura = 600
ecra_altura = 680
janela = pygame.display.set_mode(
    (ecra_largura, ecra_altura)
)
pygame.display.set_caption('Corona Vírus: O Jogo')

# Cores
cor = {
    'b': (0,0,0),# preto　黒
    'w': (255,255,255), # branco　白
    'c': (64,249,255), # ciano　シアン
    'g': (66,255,66), # verde 緑
    'g': (248,210,16), # ouro 金色
    'r': (245,23,32) # vermelho　赤
}

# Objetos do jogo
fundo = pygame.image.load('data/tela.jpg')
home = pygame.image.load('data/home_sketch.jpg')
en = pygame.image.load('data/coronga_vairus.png')
linha = pygame.Rect(0,621,600,20)
fonte = pygame.font.SysFont('calibri', 30)
titulo_on = True
enemies = []
pos = (
    [124, -76],
    [256, -76],
    [409, -76]
)
ciclo = 0
vel = 1 + ciclo//300
vida = 3
# loop
while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit here!")
            pygame.quit()
            exit()

    comando = pygame.key.get_pressed()
    if comando[pygame.K_SPACE]:
        if titulo_on:
            titulo_on = False
        else:
            found_en = False
            for c in enemies:
                if 621 < c[1] + 75 < 675:
                    found_en = True
                    enemies.remove(c)
                else:
                    pass
            if found_en == False:
                vida -= 1

    if titulo_on:
        janela.blit(home,(0,0))
    else:
        ciclo += 1
        if ciclo % 150 == 0:
            enemies.append(pos[rd(0, len(pos)-1)].copy())
        print(enemies)

        # Desenhando na tela
        timer = fonte.render(f'{ciclo//75}', False, cor['b'])
        hp = fonte.render(f'{vida}', False, cor['b'])
        janela.blit(fundo,(0,0))
        pygame.draw.rect(janela, cor['c'], linha)
        janela.blit(timer, (0, 0))
        janela.blit(hp, (0, 30))
        for c in enemies:
            janela.blit(en,c)

        # atualizando posições e deletando da tela
        tirar=[]
        for c in range(len(enemies)):
            if enemies[c][1] > 690:
                tirar.append(enemies[c])
                print(c)
            else:
                enemies[c][1] += vel + ciclo//300
        tirar.sort(reverse=True)
        for c in tirar:
            enemies.remove(c)
            vida -= 1


    # Atualizar a tela
    pygame.display.flip()
    clock.tick()
