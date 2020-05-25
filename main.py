# Author: Allan Lucas
# Python 3.8
'''
<SETUP>
:param logger: se encarrega de fazer o trackeamento de erros no jogo;
:param log: True logger ativo; False logger desativado
:param clock: se encarrega de brecar o jogo a um certo framerate
:param fps: frames por segundo, framerate*
:param ecra_largura: largura da janela
:param ecra_altura: altura da janela
:param janela: *auto-explicativo
:param cor: dicionário de cores
:param fundo: carrega a imagem do fundo
:param home: carrega a imagem da tela inicial
:param en: carrega a imagem do virus
:param music: carrega a musica
:param musica_on: para True: musica tocando; Para False: musica ainda nao tocada
:param linha: guarda o pygame.Rect() da linha para transformar em objeto
:param fonte: *auto-explicativo
:param screen: Para 'tela': tela inicial; Para 'jogo': tela do jogo; Para 'pause': Pausa o jogo em andamento
:param enemies: lista com os viruzinhos na tela
:param pos: posicoes pré-definidas dos viruzinhos
:param cycl: registra o tempo
:param ciclo: inteiro que diz quantas vezes o loop foi feito
:param vel: velocidade em função de ciclo, (1 + ciclo//300)/ 4
:param vida: *auto-explicativo
:param cycl_1: lista que guarda os três últimos estados de undefined
<LOOP>
:param comando: Se encarrega de buscar as teclas e retorna True quando pressionadas
:param tirar: Se encarrega de guardar informação dos vírus para tirar da tela
'''
from logging import Logger

import pygame
from pygame import mixer as mix
from sys import exit
from random import randint as rd
import logging
from math import trunc

# Criando e configurando logger
logging.basicConfig(
    filename='main.log',
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s - %(message)s",
    filemode='w'
)
log = False  # sem acompanhamento de erros

if log:
    logger: Logger = logging.getLogger()
if log:
    logger.debug('Logging on.')

# Preparando a Janela
if log:
    logger.debug('pygame init')
pygame.init()  # inicia o pygame
clock = pygame.time.Clock()
fps = 50  # framerate
ecra_largura = 600
ecra_altura = 680
janela = pygame.display.set_mode(
    (ecra_largura, ecra_altura)
)
pygame.display.set_caption('Corona Vírus: O Jogo')

# Cores
if log:
    logger.debug('cores')
cor = {
    'b': (0, 0, 0),  # preto　黒
    'w': (255, 255, 255),  # branco　白
    'c': (64, 249, 255),  # ciano　シアン
    'g': (66, 255, 66),  # verde 緑
    'go': (248, 210, 16),  # ouro 金色
    'r': (245, 23, 32)  # vermelho　赤
}

# Objetos do jogo
if log:
    logger.debug('Objetos do jogo')
fundo = pygame.image.load('data/tela.jpg')
home = pygame.image.load('data/home.jpg')
pause = pygame.image.load('data/pause.png')
fim = pygame.image.load('data/fim.jpg')
en = pygame.image.load('data/coronga_vairus.png')
mix.music.load('data/audio.ogg')
musica_on = False
linha = pygame.Rect(0, 621, 600, 20)
fonte = pygame.font.SysFont('calibri', 30)
screen = 'tela'
pos = (
    [125, -76],
    [267, -76],
    [409, -76]
)
enemies = []
cycl = 0
ciclo = 0  # ciclos dentro do loop
vel = 1 + ciclo / 50
vida = 5
cycl_1 = [0, 0, 0]
def draw(comeco = True, vida=0):
    if comeco:
        timer = fonte.render(f'Tempo: {ciclo // 50}s', False, cor['b'])
        hp = fonte.render(f'HP: {vida}', False, cor['b'])
        janela.blit(fundo, (0, 0))
        pygame.draw.rect(janela, cor['c'], linha)
        janela.blit(timer, (0, 0))
        janela.blit(hp, (0, 30))
        for c in enemies:
            janela.blit(en, c)
    else:
        janela.blit(fim, (0,0))
        janela.blit(fonte.render(f'Tempo: {ciclo // 50}s', False, cor['b']), (230, 450))
# loop
if log:
    logger.debug('Inicia o loop')
while True:
    vel = 1 + ciclo / 1000
    print(cycl, cycl_1)
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if log:
                logger.debug('Clicou no X\nexit')
            pygame.quit()
            exit()

    # keyboard binding
    comando = pygame.key.get_pressed()
    if comando[pygame.K_ESCAPE] and screen == 'tela':
        pygame.quit()
        exit()

    if comando[pygame.K_q] and screen == 'fim':
        screen = 'jogo'
        enemies = []
        cycl = 0
        ciclo = 0  # ciclos dentro do loop
        vel = 1 + ciclo / 50
        vida = 4
        cycl_1 = [0, 0, 0]

    if comando[pygame.K_SPACE] or comando[pygame.K_1]:
        if screen == 'tela':
            pass
        else:
            screen = 'pausa'

    if comando[pygame.K_a]:
        if screen == 'tela':
            screen = 'jogo'
        elif screen == 'pausa':
            screen = 'jogo'
        else:
            not_en = True
            for c in enemies:
                if c[0] == 125 and 621 < c[1] + 75 < 675 or 621 < c[1] < 675:
                    not_en = False
                    cycl = 0
                    enemies.remove(c)
                else:
                    pass
            if not_en:
                cycl += 1
                cycl_1.append(cycl // 30)
                if cycl_1[1] != cycl_1[2]:
                    vida -= 1
                if len(cycl_1) > 2:
                    del cycl_1[0]

    if comando[pygame.K_s]:
        if screen == 'tela':
            screen = 'jogo'
        elif screen == 'pausa':
            screen = 'jogo'
        else:
            not_en = True
            for c in enemies:
                if c[0] == 267 and 621 < c[1] + 75 < 675 or 621 < c[1] < 675:
                    not_en = False
                    cycl = 0
                    enemies.remove(c)
                else:
                    pass
            if not_en:
                cycl += 1
                cycl_1.append(cycl // 30)
                if cycl_1[1] != cycl_1[2]:
                    vida -= 1
                if len(cycl_1) > 2:
                    del cycl_1[0]

    if comando[pygame.K_d]:
        if screen == 'tela':
            screen = 'jogo'
        else:
            not_en = True
            for c in enemies:
                if c[0] == 409 and 621 < c[1] + 75 < 675 or 621 < c[1] < 675:
                    not_en = False
                    cycl = 0
                    enemies.remove(c)
                else:
                    pass
            if not_en:
                cycl += 1
                cycl_1.append(cycl // 30)
                if cycl_1[1] != cycl_1[2]:
                    vida -= 1
                if len(cycl_1) > 2:
                    del cycl_1[0]

    if screen == 'tela':
        janela.blit(home, (0, 0))
        if log:
            logger.debug('Home')
    elif screen == 'jogo':
        if vida <= 0:
            pass
        ciclo += 1
        if not musica_on:
            mix.music.play(-1)
            musica_on = True
        if log:
            logger.debug('Jogando')
        if ciclo % int(300 / vel) == 0 or ciclo == 1:
            if log:
                logger.info('Carregando inimigo na tela.')
            for c in range(rd(1, 3)):
                enemies.append(pos[rd(0, len(pos) - 1)].copy())

        # atualizando posições e deletando da tela
        tirar = []
        for c in range(len(enemies)):
            if enemies[c][1] > 690:
                tirar.append(enemies[c])
                # print(c)
            else:
                enemies[c][1] += vel
        tirar.sort(reverse=True)
        for c in tirar:
            enemies.remove(c)
            vida -= 1
        if vida <= 0:
            screen = 'fim'
        # Desenhando na tela
        draw(vida=vida)
    elif screen == 'pausa':
        draw()
        janela.blit(pause, (0, 0))


    elif screen == 'fim':
        draw(False)

    # Atualizar a tela

    pygame.display.flip()
    clock.tick(fps)
if log:
    logger.debug(
        f'''Variaveis:\nenemies = {enemies}\ncycl = {cycl}\nciclo = {ciclo}\nvel = {vel}\nvida = {vida}\ncycl_1 = {cycl_1}''')
