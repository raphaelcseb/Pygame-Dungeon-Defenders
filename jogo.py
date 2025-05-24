import pygame
import random
from pygame import mixer
from pathlib import Path

pygame.init()

info = pygame.display.Info()
tela_largura = info.current_w
tela_altura = info.current_h
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

def get_relative_dir(dir: str) -> str:
    return Path(__file__).parent.joinpath(dir)

num_faixas = 8
largura_faixa = screen_width // num_faixas
faixas_x = [i * largura_faixa + largura_faixa // 2 for i in range(num_faixas)]

my_font = pygame.font.Font(get_relative_dir('Font/BACKTO1982.TTF'), 32)
my_font_start = pygame.font.Font(get_relative_dir('Font/BACKTO1982.TTF'), 20)
small_font = pygame.font.Font(get_relative_dir('Font/BACKTO1982.TTF'), 10)