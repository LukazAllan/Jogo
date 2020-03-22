# Author: Allan Lucas
# Python 3.8

import pygame
from sys import exit
from random import randint as rd
import logging

# Criando e configurando logger
logging.basicConfig(
    filename = 'main.log',
    level = logging.DEBUG,
    format = "%(asctime)s %(levelname)s - %(message)s",
    filemode = 'w'
)
logger = logging.getLogger()
logger.debug('Logging on.')


# Preparando a Janela
logger.debug('pygame init')
pygame.init() #inicia o pygame
clock = pygame.time.Clock()
ecra_largura = 600
ecra_altura = 680
janela = pygame.display.set_mode(
    (ecra_largura, ecra_altura)
)
pygame.display.set_caption('Corona Vírus: O Jogo')

# Cores
logger.debug('cores')
cor = {
    'b': (0,0,0),# preto　黒
    'w': (255,255,255), # branco　白
    'c': (64,249,255), # ciano　シアン
    'g': (66,255,66), # verde 緑
    'g': (248,210,16), # ouro 金色
    'r': (245,23,32) # vermelho　赤
}

# Objetos do jogo
logger.debug('Objetos do jogo')
fundo = pygame.image.load('data/tela.jpg')
home = pygame.image.load('data/home_sketch.jpg')
en = pygame.image.load('data/coronga_vairus.png')
music = pygame.mixer.music.load('data/audio.ogg')
musica_on = False
linha = pygame.Rect(0,621,600,20)
fonte = pygame.font.SysFont('calibri', 30)
screen = 'tela'
enemies = []
pos = (
    [124, -76],
    [256, -76],
    [409, -76]
)
cycl = 0
ciclo = 0
vel = (1 + ciclo//300)/ 2
vida = 4
cycl_1 = ['','','']
# loop
logger.debug('Inicia o loop')
while True:

    ciclo += 1
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logger.debug('Clicou no X\nexit')
            #print("Quit here!")
            pygame.quit()
            exit()

    # keyboard binding
    comando = pygame.key.get_pressed()
    if comando[pygame.K_SPACE] or comando[pygame.K_1]:
        logger.debug('Espaço')
        if screen == 'tela':
            screen = 'jogo'
        else:
            not_en = True
            for c in enemies:
                if 621 < c[1] + 75 < 675:
                    not_en = False
                    cycl = 0
                    enemies.remove(c)
                else:
                    pass
            if not_en:
                cycl += 1
                cycl_1.append(cycl//30)
                if cycl_1[1] != cycl_1[2]:
                    vida -= 1
                if len(cycl_1) > 2:
                    del cycl_1[0]
    if comando[pygame.K_ESCAPE]:
        if screen == 'pausa':
            screen == 'jogo'
        elif screen == 'jogo':
            screen == 'pausa'
        else:
            pass

    if screen == 'tela':
        janela.blit(home,(0,0))
        logger.debug('Home')
    elif screen == 'jogo':
        if not musica_on:
            pygame.mixer.music.play(-1)
            musica_on = True
        logger.debug('Jogando')
        if ciclo % 150 == 0:
            enemies.append(pos[rd(0, len(pos)-1)].copy())
            logger.info('Carregando inimigo na tela.')
        print(cycl)

        # Desenhando na tela
        timer = fonte.render(f'Tempo: {ciclo//75}', False, cor['b'])
        hp = fonte.render(f'HP: {vida}', False, cor['b'])
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
        if vida <= 0:
            break
        logger.debug(f'''Variaveis:
enemies = {enemies}
cycl = {cycl}
ciclo = {ciclo}
Tempo = {ciclo//75}
vel = {vel}
vida = {vida}
cycl_1 = {cycl_1}
''')
    else:
        pass

    # Atualizar a tela
    pygame.display.flip()
    clock.tick()
logger.debug(f'''Variaveis:
enemies = {enemies}
cycl = {cycl}
ciclo = {ciclo}
vel = {vel}
vida = {vida}
cycl_1 = {cycl_1}
''')
