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


text_surface = my_font.render('Jogo de Desoft', False, (255, 255, 255))
text_start = my_font_start.render('Press SPACE to start Game', False, (255, 255, 255))
start_esc = my_font_start.render('ESC', False, (255, 255, 255))
tutorial_title = my_font.render('Tutorial', False, (255, 255, 255))
tutorial_text_1 = my_font_start.render('BAD - LOSE HP', False, (255, 255, 255))
tutorial_text_2 = my_font_start.render('GET COINS $$$', False, (255, 255, 255))
avatar_title = my_font.render('Avatar', False, (255, 255, 255))
game_title = my_font.render('Game', False, (255, 255, 255))

tela_de_inicio = pygame.image.load(get_relative_dir('Level maps/fundo.png'))
tela_de_inicio = pygame.transform.scale(tela_de_inicio, (screen_width, screen_height))
castle_overlay = pygame.image.load(get_relative_dir('Level maps/castle overlay.png')).convert_alpha()
castle_overlay = pygame.transform.scale(castle_overlay, (screen_width, screen_height))
background_img = pygame.image.load(get_relative_dir('Level maps/game map.png'))
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

player_sheet = pygame.image.load(get_relative_dir('Animation/jogador/Sword_Walk_full.png'))
player_attack_sheet = pygame.image.load(get_relative_dir('Animation/jogador/Sword_attack_full.png'))
player_hurt_sheet = pygame.image.load(get_relative_dir('Animation/jogador/Sword_Hurt_full.png'))
player_death_sheet = pygame.image.load(get_relative_dir('Animation/jogador/Sword_Death_full.png'))

flecha_cima = pygame.image.load(get_relative_dir('Obstacles/flecha_cima.png')).convert_alpha()
flecha_cima = pygame.transform.scale(flecha_cima, (46, 70))

flecha_baixo = pygame.image.load(get_relative_dir('Obstacles/flecha_baixo.png')).convert_alpha()
flecha_baixo = pygame.transform.scale(flecha_baixo, (46, 70))

flecha_esquerda = pygame.image.load(get_relative_dir('Obstacles/flecha_esquerda.png')).convert_alpha()
flecha_esquerda = pygame.transform.scale(flecha_esquerda, (70, 46))

flecha_direita = pygame.image.load(get_relative_dir('Obstacles/flecha_direita.png')).convert_alpha()
flecha_direita = pygame.transform.scale(flecha_direita, (70, 46))

orc1_hurt_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc1_hurt_full.png'))
orc1_attack_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc1_attack_full.png'))
orc1_body_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc1_walk_full.png'))
orc1_death_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc1_death_full.png'))

orc2_hurt_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc2_hurt_full.png'))
orc2_attack_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc2_attack_full.png'))
orc2_body_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc2_walk_full.png'))
orc2_death_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc2_death_full.png'))

orc3_hurt_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc3_hurt_full.png'))
orc3_attack_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc3_attack_full.png'))
orc3_body_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc3_walk_full.png'))
orc3_death_sprite_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/orc3_death_full.png'))

vampiro1_walk_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires1_Walk_full.png'))
vampiro1_attack_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires1_Attack_full.png'))
vampiro1_hurt_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires1_Hurt_full.png'))
vampiro1_death_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires1_Death_full.png'))

vampiro2_walk_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires2_Walk_full.png'))
vampiro2_attack_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires2_Attack_full.png'))
vampiro2_hurt_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires2_Hurt_full.png'))
vampiro2_death_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires2_Death_full.png'))

vampiro3_walk_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires3_Walk_full.png'))
vampiro3_attack_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires3_Attack_full.png'))
vampiro3_hurt_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires3_Hurt_full.png'))
vampiro3_death_sheet = pygame.image.load(get_relative_dir('Animation/Enemy/Vampires3_Death_full.png'))

coin_img = pygame.image.load(get_relative_dir('Obstacles/coin.png'))
coin_img = pygame.transform.scale(coin_img, (32, 32))
barrel_img = pygame.image.load(get_relative_dir('Obstacles/barrel.png'))
barrel_img = pygame.transform.scale(barrel_img, (64, 64))

