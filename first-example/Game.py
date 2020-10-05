import pygame
from colors import COLORS
from pygame.locals import * # K_UP, K_DOWN, ...
from Player import Player 

class Game:
    def __init__(self):
        # tela do jogo com 500x500 e centro da tela
        self.window = pygame.display.set_mode((500, 500))
        # nosso jogador (um retângulo mto intrépido)
        self.player = Player()

    def run(self):
        # Fundo da tela preto
        self.window.fill(COLORS["black"])

        # Desenha jogador na tela
        self.player.update()
        self.window.blit(self.player.surf, self.player.rect)

        # update de todo o display
        pygame.display.flip()
