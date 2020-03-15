# Author: Allan Lucas
#

import pygame
from sys import exit
from json import load

# Carregando Dados
with open('data.json', 'r', encoding='utf-8') as raw:
    data = load(raw)

# Preparando a Janela
pygame.init() #inicia o pygame
clock = pygame.time.Clock()
ecra_largura = 600
ecra_altura = 680
janela = pygame.display.set_mode(
    (ecra_largura, ecra_altura)
)
pygame.display.set_caption('Japonês')

# Cores
cor = {
    'b': (0,0,0),# preto
    'w': (255,255,255), # branco
    'c': (64,249,255), # ciano
    'g': (66,255,66), # verde
    'g': (248,210,16), # 金色
    'r': (245,23,32), # vermelho
    'bk': (30,70,130) # only for bk
}

# Objetos do jogo
fundo = pygame.image.load('data/fundo.jpg')
linha = pygame.Rect(0,621,600,20)

fonte = pygame.font.SysFont('NSinSum', 80)
palavra = fonte.render('enpitsu', False, cor['w'])
pos_palavra = palavra.get_rect()
pos_palavra.center = (138,40)

# loop
while True:
    #pygame.time.delay(50)
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit here!")
            pygame.quit()
            exit()

    # Desenhando na tela
    janela.fill(cor['g'])
    janela.blit(fundo,(0,95))
    pygame.draw.rect(janela, (245,23,32), linha)
    janela.blit(palavra,pos_palavra)


    # Atualizar a tela
    pygame.display.flip()
    clock.tick()
