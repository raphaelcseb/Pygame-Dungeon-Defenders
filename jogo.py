import pygame
import random
from pygame import mixer
from pathlib import Path

pygame.init()
pygame.mixer.init()

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

pygame.mixer.music.load('Sons\Overworld_Hyrule.mp3')
pygame.mixer.music.set_volume(0.4)

def load_orc_frames(sheet, frame_width=64, frame_height=64, scale=4, rows=4, cols=6):
    directions = ['down', 'up', 'left', 'right']
    frames = {dir: [] for dir in directions}
    for y, dir in enumerate(directions):
        for x in range(cols):
            try:
                frame = sheet.subsurface(pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height))
                scaled_frame = pygame.transform.scale(frame, (frame_width * scale, frame_height * scale))
                frames[dir].append(scaled_frame)
            except Exception as e:
                debug_frame = pygame.Surface((frame_width * scale, frame_height * scale))
                debug_frame.fill((255, 0, 0))
                frames[dir].append(debug_frame)
    return frames


def load_player_sprites(sheet, frame_width, frame_height, scale=2):
    directions = ['down', 'left', 'right', 'up']
    sprites = {dir: [] for dir in directions}
    for y, dir in enumerate(directions):
        for x in range(3):
            frame = sheet.subsurface(pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height))
            scaled_frame = pygame.transform.scale(frame, (frame_width * scale, frame_height * scale))
            sprites[dir].append(scaled_frame)
    return sprites

player_sprites = load_player_sprites(player_sheet, 64, 64, scale=4)


def load_attack_frames(sheet, frame_width=64, frame_height=64, rows=4, cols=8, scale=4):
    directions = ['down', 'left', 'right', 'up']
    frames = {dir: [] for dir in directions}
    for y, dir in enumerate(directions):
        for x in range(cols):
            frame = sheet.subsurface(pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height))
            scaled = pygame.transform.scale(frame, (frame_width * scale, frame_height * scale))
            frames[dir].append(scaled)
    return frames

player_attack_frames = load_attack_frames(player_attack_sheet)
player_hurt_frames = load_attack_frames(player_hurt_sheet, frame_width=64, frame_height=64, rows=4, cols=5, scale=4)
player_death_frames = load_attack_frames(player_death_sheet, frame_width=64, frame_height=64, rows=4, cols=7, scale=4)

orc1_attack_frames = load_orc_frames(orc1_attack_sprite_sheet)
orc1_body_frames = load_orc_frames(orc1_body_sprite_sheet)
orc1_hurt_frames = load_orc_frames(orc1_hurt_sprite_sheet)
orc1_death_frames = load_orc_frames(orc1_death_sprite_sheet)

orc2_attack_frames = load_orc_frames(orc2_attack_sprite_sheet)
orc2_body_frames = load_orc_frames(orc2_body_sprite_sheet)
orc2_hurt_frames = load_orc_frames(orc2_hurt_sprite_sheet)
orc2_death_frames = load_orc_frames(orc2_death_sprite_sheet)

orc3_attack_frames = load_orc_frames(orc3_attack_sprite_sheet)
orc3_body_frames = load_orc_frames(orc3_body_sprite_sheet)
orc3_hurt_frames = load_orc_frames(orc3_hurt_sprite_sheet)
orc3_death_frames = load_orc_frames(orc3_death_sprite_sheet)

vampiro1_walk_frames = load_orc_frames(vampiro1_walk_sheet)
vampiro1_attack_frames = load_orc_frames(vampiro1_attack_sheet)
vampiro1_hurt_frames = load_orc_frames(vampiro1_hurt_sheet, cols=4)
vampiro1_death_frames = load_orc_frames(vampiro1_death_sheet, cols=11)

vampiro2_walk_frames = load_orc_frames(vampiro2_walk_sheet)
vampiro2_attack_frames = load_orc_frames(vampiro2_attack_sheet)
vampiro2_hurt_frames = load_orc_frames(vampiro2_hurt_sheet, cols=4)
vampiro2_death_frames = load_orc_frames(vampiro2_death_sheet, cols=11)

vampiro3_walk_frames = load_orc_frames(vampiro3_walk_sheet)
vampiro3_attack_frames = load_orc_frames(vampiro3_attack_sheet)
vampiro3_hurt_frames = load_orc_frames(vampiro3_hurt_sheet, cols=4)
vampiro3_death_frames = load_orc_frames(vampiro3_death_sheet, cols=11)

class DroppedItem:
    def __init__(self, x, y, item_type,falling=False):
        self.x = x
        self.y = y
        self.type = item_type
        self.spawn_time = pygame.time.get_ticks()
        self.blink_timer = 0
        self.visible = True
        self.health = 2 if item_type == "barrel" else 1
        self.invulnerable_until = pygame.time.get_ticks() + 2000
        self.rect = pygame.Rect(x, y, 32, 32) if item_type == "coin" else pygame.Rect(x, y, 64, 64)
        self.falling = False
        self.fall_speed = 3
        self.stop_y = screen_height - 200
        self.falling = falling

    def update(self):
        current_time = pygame.time.get_ticks()
        lifetime = current_time - self.spawn_time

        if self.type == "coin" and self.falling:
            self.y += self.fall_speed
            if self.y >= self.stop_y:
                self.y = self.stop_y
                self.falling = False

        self.rect.topleft = (self.x, self.y)

        if self.type == "coin":
            if lifetime > 9000:
                self.blink_timer += pygame.time.get_ticks() - (self.spawn_time + 3000)
                if self.blink_timer > 200:
                    self.visible = not self.visible
                    self.blink_timer = 0
            return lifetime < 11000

        elif self.type == "barrel":
            return True

    
    def take_damage(self):
        if pygame.time.get_ticks() < self.invulnerable_until:
            return False
        self.health -= 1
        self.invulnerable_until = pygame.time.get_ticks() + 300  
        return self.health <= 0


    def draw(self, surface, show_hitbox=False):
        if not self.visible and self.type == "coin":
            return

        if self.type == "coin":
            surface.blit(coin_img, self.rect.topleft)
        elif self.type == "barrel":
            surface.blit(barrel_img, self.rect.topleft)

        if show_hitbox:
            pygame.draw.rect(surface, (0, 255, 0), self.rect, 2)

class OrcBase:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame_index = 0
        self.current_frames = self.walk_frames
        self.frame_delay = 0.3
        self.frame_timer = 0
        self.parado = False
        self.atacando = False
        self.hurt = False
        self.hurt_timer = 0
        self.hurt_duration = 500
        self.morto = False
        self.death_timer = 0
        self.death_duration = 1000
        self.death_animation_complete = False
        self.direcao = 'down'
        self.ultimo_ataque_castelo = 0
        self.intervalo_ataque_castelo = 1000



    def update(self, dt, player_pos):
        if self.morto:
            self.frame_timer += dt
            if self.frame_timer >= self.frame_delay:
                direcao_frames = self.current_frames.get(self.direcao, list(self.current_frames.values())[0])
                if self.frame_index < len(direcao_frames) - 1:
                    self.frame_index += 1
                    self.frame_timer = 0
                else:
                    self.death_animation_complete = True
            return

        if getattr(self, "post_special_block", False):
            return


        if self.morto:
            self.frame_timer += dt
            if self.frame_timer >= self.frame_delay:
                direcao_frames = self.current_frames.get(self.direcao, list(self.current_frames.values())[0])
                if self.frame_index < len(direcao_frames) - 1:
                    self.frame_index += 1
                    self.frame_timer = 0
                else:
                    self.death_animation_complete = True
            return

        if self.hurt:
            if pygame.time.get_ticks() - self.hurt_timer > self.hurt_duration:
                self.hurt = False
                self.set_animacao("andar")

        if not self.parado:
            player_x, player_y = player_pos
            dist_x = player_x - self.x
            dist_y = player_y - self.y
            distancia = (dist_x**2 + dist_y**2) ** 0.5

            if distancia < getattr(self, 'follow_range', 1000):
                norm_x = dist_x / distancia
                norm_y = dist_y / distancia
                self.x += norm_x * self.speed
                self.y += norm_y * self.speed

                if abs(dist_y) > abs(dist_x):
                    self.direcao = 'down' if dist_y > 0 else 'up'
                else:
                    self.direcao = 'right' if dist_x > 0 else 'left'
            else:
                self.y += self.speed
                self.direcao = 'down'

            if self.y > screen_height - 325:
                self.y = screen_height - 325
                agora = pygame.time.get_ticks()
                if not self.parado:
                    self.set_animacao("atacar")
                    self.parado = True

                if agora - self.ultimo_ataque_castelo >= self.intervalo_ataque_castelo:
                    GameState.castle_HP -= self.damage
                    self.ultimo_ataque_castelo = agora

                    if GameState.castle_HP <= 0:
                        GameState.player_dead = True
                        GameState.player_death_timer = pygame.time.get_ticks()

        self.frame_timer += dt
        if self.frame_timer >= self.frame_delay:
            self.frame_index = (self.frame_index + 1) % len(self.current_frames[self.direcao])
            self.frame_timer = 0



    def draw(self, surface, show_hitbox=False):
        frame_list = self.current_frames.get(self.direcao) or list(self.current_frames.values())[0]
        frame = frame_list[int(self.frame_index)]

        if self.hurt and not self.morto:
            temp_surface = pygame.Surface((frame.get_width(), frame.get_height()), pygame.SRCALPHA)
            temp_surface.blit(frame, (0, 0))
            temp_surface.fill((255, 0, 0, 100), special_flags=pygame.BLEND_MULT)
            surface.blit(temp_surface, (self.x, self.y))
        else:
            surface.blit(frame, (self.x, self.y))

        if show_hitbox:
            rect = pygame.Rect(self.x + 64, self.y + 64, 128, 128)
            pygame.draw.rect(surface, (0, 255, 0), rect, 2)


    def set_animacao(self, tipo):
        if self.morto:
            return

        if tipo == "andar":
            self.current_frames = self.walk_frames
        elif tipo == "atacar":
            self.current_frames = self.attack_frames
        elif tipo == "hurt":
            self.current_frames = self.hurt_frames
            self.hurt = True
            self.hurt_timer = pygame.time.get_ticks()
        elif tipo == "morrer":
            self.current_frames = self.death_frames
            self.morto = True
            self.frame_index = 0
            self.death_timer = pygame.time.get_ticks()

class Orc1Enemy(OrcBase):
    def __init__(self, x, y):
        self.speed = 2
        self.hurt_frames = orc1_hurt_frames
        self.walk_frames = orc1_body_frames
        self.attack_frames = orc1_attack_frames
        self.death_frames = orc1_death_frames
        self.hp = 2
        self.damage = 10
        self.type = "orc1"
        self.follow_range = 300
        super().__init__(x, y)

class Orc2Enemy(OrcBase):
    def __init__(self, x, y):
        self.speed = 4
        self.hurt_frames = orc2_hurt_frames
        self.walk_frames = orc2_body_frames
        self.attack_frames = orc2_attack_frames
        self.death_frames = orc2_death_frames
        self.hp = 1
        self.damage = 8
        self.type = "orc2"
        self.follow_range = 300
        super().__init__(x, y)

    def on_death(self):
        return DroppedItem(self.x + 112, self.y + 112, "coin")

class Orc3Enemy(OrcBase):
    def __init__(self, x, y):
        self.speed = 3
        self.hurt_frames = orc3_hurt_frames
        self.walk_frames = orc3_body_frames
        self.attack_frames = orc3_attack_frames
        self.death_frames = orc3_death_frames
        self.hp = 3
        self.damage = 12
        self.type = "orc3"
        self.follow_range = 300
        super().__init__(x, y)

    def on_death(self):
        return DroppedItem(self.x + 96, self.y + 96, "barrel")

class VampiroBoss(OrcBase):
    def __init__(self, x, y, walk_frames, attack_frames, hurt_frames, death_frames, level=1):
        self.walk_frames = walk_frames
        self.attack_frames = attack_frames
        self.hurt_frames = hurt_frames
        self.death_frames = death_frames
        self.hp = 30 + level * 10
        self.max_hp = self.hp
        self.damage = 20 + level * 5
        self.type = f"vampiro{level}"
        self.speed = 1 + level * 0.2
        super().__init__(x, y)
        self.level = level
        self.special_attack_lines = []        
        self.special_attack_phase = 0
        self.last_attack_time = pygame.time.get_ticks()
        self.special_attack_interval = 500
        self.special_attack_cooldown = 8000 
        self.in_attack_sequence = False
        self.post_attack_delay = 2500
        self.post_attack_timer = 0
        self.special_attack_timer = pygame.time.get_ticks()
        self.post_special_block = False
        self.post_special_block_timer = 0
        self.post_special_block_duration = 2500
        self.follow_range = 150000
        
    def on_death(self):
        return DroppedItem(self.x + 112, self.y + 112, "coin")



    def cast_circle_attack(self, offset_angle=0):
        for angle in range(offset_angle, 360 + offset_angle, 30):
            direction = pygame.math.Vector2(1, 0).rotate(angle)
            projectile = {
                'x': self.x + 128,
                'y': self.y + 128,
                'dx': direction.x * 8,
                'dy': direction.y * 8,
                'timer': pygame.time.get_ticks(),
                'damage': 10 + self.level * 5,
                'ignora_imunidade': True 
            }
            special_effects.append(projectile)

    def handle_special_attack(self):
        now = pygame.time.get_ticks()

        if self.post_special_block and now - self.post_special_block_timer >= self.post_special_block_duration:
            self.post_special_block = False

        if self.in_attack_sequence:
            if self.special_attack_phase < 3 and now - self.last_attack_time >= self.special_attack_interval:
                offset = 0 if self.special_attack_phase % 2 == 0 else 15
                self.cast_circle_attack(offset_angle=offset)
                self.last_attack_time = now
                self.special_attack_phase += 1

                if self.special_attack_phase == 3:
                    self.post_attack_timer = now
                    self.parado = True

                    self.post_special_block = True
                    self.post_special_block_timer = now


            elif self.special_attack_phase == 3 and now - self.post_attack_timer >= self.post_attack_delay:
                self.in_attack_sequence = False
                self.special_attack_timer = now
                self.parado = False

                self.post_special_block = True
                self.post_special_block_timer = now

        elif now - self.special_attack_timer >= self.special_attack_cooldown:
            self.special_attack_phase = 0
            self.in_attack_sequence = True
            self.last_attack_time = now


    def draw_health_bar(self, surface):
        bar_width = 600
        bar_height = 25
        bar_x = screen_width // 2 - bar_width // 2
        bar_y = 20
        pygame.draw.rect(surface, (255, 255, 255), (bar_x - 2, bar_y - 2, bar_width + 4, bar_height + 4))
        filled = int((self.hp / self.max_hp) * bar_width)
        pygame.draw.rect(surface, (221, 160, 221), (bar_x, bar_y, filled, bar_height))
    
    def draw_special_attack(self, surface):
        for line in self.special_attack_lines:
            pygame.draw.line(
                surface, 
                (255, 0, 0),
                (line['start_x'], line['start_y']),
                (line['end_x'], line['end_y']),
                3
            )

class Vampiro1Boss(VampiroBoss):
    def __init__(self, x, y):
        super().__init__(x, y,
                         vampiro1_walk_frames,
                         vampiro1_attack_frames,
                         vampiro1_hurt_frames,
                         vampiro1_death_frames,
                         level=1)

class Vampiro2Boss(VampiroBoss):
    def __init__(self, x, y):
        super().__init__(x, y,
                         vampiro2_walk_frames,
                         vampiro2_attack_frames,
                         vampiro2_hurt_frames,
                         vampiro2_death_frames,
                         level=2)


class Vampiro3Boss(VampiroBoss):
    def __init__(self, x, y):
        super().__init__(x, y,
                         vampiro3_walk_frames,
                         vampiro3_attack_frames,
                         vampiro3_hurt_frames,
                         vampiro3_death_frames,
                         level=3)

def gerar_orcs_em_faixas(qtd=3):
    orcs = []
    for _ in range(qtd):
        faixa = random.choice(faixas_x)
        x = faixa - 128
        y = random.randint(-600, -100)
        x = max(0, min(x, screen_width - 256))

        tipo_orc = random.choices(
            ['orc1', 'orc2', 'orc3'],
            weights=[0.5, 0.3, 0.2],
            k=1
        )[0]

        if tipo_orc == 'orc1':
            orc = Orc1Enemy(x, y)
        elif tipo_orc == 'orc2':
            orc = Orc2Enemy(x, y)
        elif tipo_orc == 'orc3':
            orc = Orc3Enemy(x, y)

        orcs.append(orc)
    return orcs

