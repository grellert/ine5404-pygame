# Primeiro exemplo com PyGame
# versão adaptada de: https://realpython.com/pygame-a-primer/

# importando PyGame
import pygame
from pygame.locals import * # K_UP, K_DOWN, ...
from Player import Player 
from Game import Game

pygame.init()

game = Game()

# Game loop: laço que termina quando a janela é fechada (evento)
running = True
while running:
    game.run()
    
    # pygame.event.get() retorna uma lista com os eventos da janela
    for event in pygame.event.get():
        # janela fechada
        if event.type == QUIT:
            running = False
        # tecla pressionada
        if event.type == KEYDOWN:
            # tecla ESC termina o jogo
            if event.key == K_ESCAPE:
                running = False

# Feito!
pygame.quit()

# exemplos pra desenhar diretamente na tela sem Sprites:
# desenha um círculo azul com centro no meio da tela e raio 75px
#pygame.draw.circle(screen, colors["blue"], screen_center, 75)
