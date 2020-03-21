# Author: Allan Lucas
#

import pygame
from sys import exit
from json import load
from random import choice as rd

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

fonte = pygame.font.SysFont('calibri', 80)
titulo = fonte.render('Corona Vírus', False, cor['b'])
pos_titulo = titulo.get_rect()
pos_titulo.center = (300,125)
fonte = pygame.font.SysFont('calibri', 30)
stt = [fonte.render(c, False, cor['b']) for c in ('Para se livrar desse vírus,','pressione ESPAÇO quando','passar pela linha azul!', 'Pressione ESPAÇO para começar')]

stt_size = [c.get_rect() for c in stt]
size = ((298,264),(290,299), (300,333), (300,582))
for c in range(len(stt)):
    stt_size[c].center = size[c]

titulo_on = True
enemies = []
pos = (
    [124, -76],
    [256, -76],
    [409, -76]
)
ciclo = 0
# loop
while True:
    #pygame.time.delay(50)
    # print(ciclo)
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
            pass
    if comando[pygame.K_UP]:
        pos[1] -=  1
    if comando[pygame.K_DOWN]:
        pos[1] +=  1
    if comando[pygame.K_LEFT]:
        pos[0] -=  1
    if comando[pygame.K_RIGHT]:
        pos[0] +=  1
    if comando[pygame.K_1]:
        print(pos)
    # [124, 2], [256, 2],[409, 543]
    # Desenhando na tela
    if titulo_on:
        # janela.blit(titulo,pos_titulo)
        # for c in range(len(stt)):
        #     janela.blit(stt[c],stt_size[c])
        janela.blit(home,(0,0))
    else:
        ciclo += 1
        if ciclo % 150 == 0:
            enemies.append(rd(pos))
        print(enemies)
        timer = fonte.render(f'{ciclo//75}', False, cor['b'])
        janela.blit(fundo,(0,0))
        pygame.draw.rect(janela, cor['c'], linha)
        janela.blit(timer, (0,0))
        for c in enemies:
            janela.blit(en,c)
        # atualizando posições e deletando da tela
        tirar=[]
        for c in range(len(enemies)):
            if enemies[c][1] > 690:
                tirar.append(c)
                print(c)
            else:
                enemies[c][1] += 1
        if len(tirar) != 0:
            for c in tirar:
                enemies.pop(index=c)


    # Atualizar a tela
    pygame.display.flip()
    clock.tick()
