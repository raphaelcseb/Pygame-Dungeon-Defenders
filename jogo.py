import pygame
import random
from pygame import mixer
from pathlib import Path

pygame.init()

info = pygame.display.Info()
tela_largura = info.current_w
tela_altura = info.current_h
tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
largura_tela, altura_tela = tela.get_size()