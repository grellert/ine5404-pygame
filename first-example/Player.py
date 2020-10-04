import pygame
from pygame.locals import * # K_UP, K_DOWN, ...
from colors import COLORS

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(COLORS["dodgerblue"])
        self.rect = self.surf.get_rect()
    
    # método que atualiza nosso player
    def update(self):
        # key.get_pressed() retorna um dicionário com todos os eventos de tecla
        # os valores são true se a tecla foi pressionada, falso c.c.
        pressed_keys = pygame.key.get_pressed()
        
        # vamos testar as teclas de movimento
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)