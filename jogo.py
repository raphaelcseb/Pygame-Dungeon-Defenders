import pygame
import random
from pygame import mixer
from pathlib import Path

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
tela_largura = info.current_w
tela_altura = info.current_h
tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
tela_largura, tela_altura = tela.get_size()

def direcao_relativa(dir: str) -> str:
    return Path(__file__).parent.joinpath(dir)

num_faixas = 8
largura_faixa = tela_largura // num_faixas
faixas_x = [i * largura_faixa + largura_faixa // 2 for i in range(num_faixas)]

my_font = pygame.font.Font(direcao_relativa('Font/BACKTO1982.TTF'), 32)
my_font_start = pygame.font.Font(direcao_relativa('Font/BACKTO1982.TTF'), 20)
small_font = pygame.font.Font(direcao_relativa('Font/BACKTO1982.TTF'), 10)

tela_de_inicio = pygame.image.load(direcao_relativa('Level maps/fundo.png'))
tela_de_inicio = pygame.transform.scale(tela_de_inicio, (tela_largura, tela_altura))
overlay_castelo = pygame.image.load(direcao_relativa('Level maps/castle overlay.png')).convert_alpha()
overlay_castelo = pygame.transform.scale(overlay_castelo, (tela_largura, tela_altura))
imagem_de_fundo = pygame.image.load(direcao_relativa('Level maps/game map.png'))
imagem_de_fundo = pygame.transform.scale(imagem_de_fundo, (tela_largura, tela_altura))

player_folha_sprites = pygame.image.load(direcao_relativa('Animation/jogador/Sword_Walk_full.png'))
player_ataque_sprites = pygame.image.load(direcao_relativa('Animation/jogador/Sword_attack_full.png'))
player_machucado_sprites = pygame.image.load(direcao_relativa('Animation/jogador/Sword_Hurt_full.png'))
player_morto_sprites = pygame.image.load(direcao_relativa('Animation/jogador/Sword_Death_full.png'))

flecha_cima = pygame.image.load(direcao_relativa('Obstacles/flecha_cima.png')).convert_alpha()
flecha_cima = pygame.transform.scale(flecha_cima, (46, 70))

flecha_baixo = pygame.image.load(direcao_relativa('Obstacles/flecha_baixo.png')).convert_alpha()
flecha_baixo = pygame.transform.scale(flecha_baixo, (46, 70))

flecha_esquerda = pygame.image.load(direcao_relativa('Obstacles/flecha_esquerda.png')).convert_alpha()
flecha_esquerda = pygame.transform.scale(flecha_esquerda, (70, 46))

flecha_direita = pygame.image.load(direcao_relativa('Obstacles/flecha_direita.png')).convert_alpha()
flecha_direita = pygame.transform.scale(flecha_direita, (70, 46))

orc1_machucado_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc1_hurt_full.png'))
orc1_ataque_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc1_attack_full.png'))
orc1_corpo_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc1_walk_full.png'))
orc1_morte_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc1_death_full.png'))

orc2_machucado_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc2_hurt_full.png'))
orc2_ataque_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc2_attack_full.png'))
orc2_corpo_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc2_walk_full.png'))
orc2_morte_spites = pygame.image.load(direcao_relativa('Animation/Enemy/orc2_death_full.png'))

orc3_machucado_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc3_hurt_full.png'))
orc3_ataque_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc3_attack_full.png'))
orc3_corpo_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc3_walk_full.png'))
orc3_morte_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/orc3_death_full.png'))

vampiro1_andando_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires1_Walk_full.png'))
vampiro1_ataque_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires1_Attack_full.png'))
vampiro1_machucado_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires1_Hurt_full.png'))
vampiro1_morte_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires1_Death_full.png'))

vampiro2_andando_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires2_Walk_full.png'))
vampiro2_ataque_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires2_Attack_full.png'))
vampiro2_machucado_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires2_Hurt_full.png'))
vampiro2_morte_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires2_Death_full.png'))

vampiro3_andando_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires3_Walk_full.png'))
vampiro3_ataque_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires3_Attack_full.png'))
vampiro3_machucado_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires3_Hurt_full.png'))
vampiro3_morte_sprites = pygame.image.load(direcao_relativa('Animation/Enemy/Vampires3_Death_full.png'))

imagem_moeda = pygame.image.load(direcao_relativa('Obstacles/coin.png'))
imagem_moeda = pygame.transform.scale(imagem_moeda, (32, 32))
imagem_barril = pygame.image.load(direcao_relativa('Obstacles/barrel.png'))
imagem_barril = pygame.transform.scale(imagem_barril, (64, 64))

#Carregando os sons do jogo
pygame.mixer.music.load('Sons\Overworld_Hyrule.mp3') #Múscia de fundo em loop 
pygame.mixer.music.set_volume(0.4)
espada_som = pygame.mixer.Sound('Sons\sword_cut.mp3')
som_compra = pygame.mixer.Sound('Sons\purchase_sound.mp3')




def carrega_orc_frames(sheet, largura_frame=64, altura_frame=64, escala=4, linhas=4, colunas=6):
    direcoes = ['down', 'up', 'left', 'right']
    frames = {dir: [] for dir in direcoes}
    for y, dir in enumerate(direcoes):
        for x in range(colunas):
            try:
                frame = sheet.subsurface(pygame.Rect(x * largura_frame, y * altura_frame, largura_frame, altura_frame))
                scaled_frame = pygame.transform.scale(frame, (largura_frame * escala, altura_frame * escala))
                frames[dir].append(scaled_frame)
            except Exception as e:
                debug_frame = pygame.Surface((largura_frame * escala, altura_frame * escala))
                debug_frame.fill((255, 0, 0))
                frames[dir].append(debug_frame)
    return frames


def carrega_player_sprites(sheet, frame_width, frame_height, scale=2):
    direcoes = ['down', 'left', 'right', 'up']
    sprites = {dir: [] for dir in direcoes}
    for y, dir in enumerate(direcoes):
        for x in range(3):
            frame = sheet.subsurface(pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height))
            scaled_frame = pygame.transform.scale(frame, (frame_width * scale, frame_height * scale))
            sprites[dir].append(scaled_frame)
    return sprites

player_sprites = carrega_player_sprites(player_folha_sprites, 64, 64, scale=4)


def carrega_ataque_frames(sheet, frame_width=64, frame_height=64, rows=4, cols=8, scale=4):
    direcoes = ['down', 'left', 'right', 'up']
    frames = {dir: [] for dir in direcoes}
    for y, dir in enumerate(direcoes):
        for x in range(cols):
            frame = sheet.subsurface(pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height))
            scaled = pygame.transform.scale(frame, (frame_width * scale, frame_height * scale))
            frames[dir].append(scaled)
    return frames

player_ataque_frames = carrega_ataque_frames(player_ataque_sprites)
player_machucado_frames = carrega_ataque_frames(player_machucado_sprites, frame_width=64, frame_height=64, rows=4, cols=5, scale=4)
player_frames_morte = carrega_ataque_frames(player_morto_sprites, frame_width=64, frame_height=64, rows=4, cols=7, scale=4)

orc1_ataque_frames = carrega_orc_frames(orc1_ataque_sprites)
orc1_corpo_frames = carrega_orc_frames(orc1_corpo_sprites)
orc1_machucado_frames = carrega_orc_frames(orc1_machucado_sprites)
orc1_morte_frames = carrega_orc_frames(orc1_morte_sprites)

orc2_ataque_frames = carrega_orc_frames(orc2_ataque_sprites)
orc2_corpo_frames = carrega_orc_frames(orc2_corpo_sprites)
orc2_machucado_frames = carrega_orc_frames(orc2_machucado_sprites)
orc2_morte_frames = carrega_orc_frames(orc2_morte_spites)

orc3_ataque_frames = carrega_orc_frames(orc3_ataque_sprites)
orc3_corpo_frames = carrega_orc_frames(orc3_corpo_sprites)
orc3_machucado_frames = carrega_orc_frames(orc3_machucado_sprites)
orc3_morte_frames = carrega_orc_frames(orc3_morte_sprites)

vampiro1_andando_frames = carrega_orc_frames(vampiro1_andando_sprites)
vampiro1_ataque_frames = carrega_orc_frames(vampiro1_ataque_sprites)
vampiro1_machucado_frames = carrega_orc_frames(vampiro1_machucado_sprites, colunas=4)
vampiro1_morte_frames = carrega_orc_frames(vampiro1_morte_sprites, colunas=11)

vampiro2_andando_frames = carrega_orc_frames(vampiro2_andando_sprites)
vampiro2_ataque_frames = carrega_orc_frames(vampiro2_ataque_sprites)
vampiro2_machucado_frames = carrega_orc_frames(vampiro2_machucado_sprites, colunas=4)
vampiro2_morte_frames = carrega_orc_frames(vampiro2_morte_sprites, colunas=11)

vampiro3_andando_frames = carrega_orc_frames(vampiro3_andando_sprites)
vampiro3_ataque_frames = carrega_orc_frames(vampiro3_ataque_sprites)
vampiro3_machucado_frames = carrega_orc_frames(vampiro3_machucado_sprites, colunas=4)
vampiro3_morte_frames = carrega_orc_frames(vampiro3_morte_sprites, colunas=11)

class itemdropado:
    def __init__(self, x, y, tipo_item,caindo=False):
        self.x = x
        self.y = y
        self.tipo = tipo_item
        self.spawn_tempo = pygame.time.get_ticks()
        self.piscar_timer = 0
        self.visivel = True
        self.vida = 2 if tipo_item == "barril" else 1
        self.invulneravel_ate = pygame.time.get_ticks() + 2000
        self.rect = pygame.Rect(x, y, 32, 32) if tipo_item == "moeda" else pygame.Rect(x, y, 64, 64)
        self.caindo = False
        self.velocidade_cair = 3
        self.parar_y = tela_altura - 200
        self.caindo = caindo

    def update(self):
        tempo_atual = pygame.time.get_ticks()
        tempo_de_vida = tempo_atual - self.spawn_tempo

        if self.tipo == "moeda" and self.caindo:
            self.y += self.velocidade_cair
            if self.y >= self.parar_y:
                self.y = self.parar_y
                self.caindo = False

        self.rect.topleft = (self.x, self.y)

        if self.tipo == "moeda":
            if tempo_de_vida > 9000:
                self.piscar_timer += pygame.time.get_ticks() - (self.spawn_tempo + 3000)
                if self.piscar_timer > 200:
                    self.visivel = not self.visivel
                    self.piscar_timer = 0
            return tempo_de_vida < 11000

        elif self.tipo == "barril":
            return True

    
    def leva_dano(self):
        if pygame.time.get_ticks() < self.invulneravel_ate:
            return False
        self.vida -= 1
        self.invulneravel_ate = pygame.time.get_ticks() + 300  
        return self.vida <= 0


    def desenha(self, surface, show_hitbox=False):
        if not self.visivel and self.tipo == "moeda":
            return

        if self.tipo == "moeda":
            surface.blit(imagem_moeda, self.rect.topleft)
        elif self.tipo == "barril":
            surface.blit(imagem_barril, self.rect.topleft)

        if show_hitbox:
            pygame.draw.rect(surface, (0, 255, 0), self.rect, 2)

class OrcBase:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame_index = 0
        self.frame_atual = self.walk_frames
        self.frame_delay = 0.3
        self.frame_timer = 0
        self.parado = False
        self.atacando = False
        self.machucado = False
        self.machucado_timer = 0
        self.machucado_duracao = 500
        self.morto = False
        self.morto_timer = 0
        self.morto_duracao = 1000
        self.animacao_de_morte = False
        self.direcao = 'down'
        self.ultimo_ataque_castelo = 0
        self.intervalo_ataque_castelo = 1000



    def update(self, dt, player_pos):
        if self.morto:
            self.frame_timer += dt
            if self.frame_timer >= self.frame_delay:
                direcao_frames = self.frame_atual.get(self.direcao, list(self.frame_atual.values())[0])
                if self.frame_index < len(direcao_frames) - 1:
                    self.frame_index += 1
                    self.frame_timer = 0
                else:
                    self.animacao_de_morte = True
            return

        if getattr(self, "post_special_block", False):
            return


        if self.morto:
            self.frame_timer += dt
            if self.frame_timer >= self.frame_delay:
                direcao_frames = self.frame_atual.get(self.direcao, list(self.frame_atual.values())[0])
                if self.frame_index < len(direcao_frames) - 1:
                    self.frame_index += 1
                    self.frame_timer = 0
                else:
                    self.animacao_de_morte = True
            return

        if self.machucado:
            if pygame.time.get_ticks() - self.machucado_timer > self.machucado_duracao:
                self.machucado = False
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

            if self.y > tela_altura - 325:
                self.y = tela_altura - 325
                agora = pygame.time.get_ticks()
                if not self.parado:
                    self.set_animacao("atacar")
                    self.parado = True

                if agora - self.ultimo_ataque_castelo >= self.intervalo_ataque_castelo:
                    estado_de_jogo.hp_castelo -= self.damage
                    self.ultimo_ataque_castelo = agora

                    if estado_de_jogo.hp_castelo <= 0:
                        estado_de_jogo.player_morto = True
                        estado_de_jogo.player_morto_timer = pygame.time.get_ticks()

        self.frame_timer += dt
        if self.frame_timer >= self.frame_delay:
            self.frame_index = (self.frame_index + 1) % len(self.frame_atual[self.direcao])
            self.frame_timer = 0



    def desenha(self, surface, show_hitbox=False):
        frame_list = self.frame_atual.get(self.direcao) or list(self.frame_atual.values())[0]
        frame = frame_list[int(self.frame_index)]

        if self.machucado and not self.morto:
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
            self.frame_atual = self.walk_frames
        elif tipo == "atacar":
            self.frame_atual = self.attack_frames
        elif tipo == "hurt":
            self.frame_atual = self.hurt_frames
            self.machucado = True
            self.machucado_timer = pygame.time.get_ticks()
        elif tipo == "morrer":
            self.frame_atual = self.death_frames
            self.morto = True
            self.frame_index = 0
            self.morto_timer = pygame.time.get_ticks()

class Orc1Enemy(OrcBase):
    def __init__(self, x, y):
        self.velocidade = 2
        self.machucado_frames = orc1_machucado_frames
        self.andando_frames = orc1_corpo_frames
        self.ataque_frames = orc1_ataque_frames
        self.morte_frames = orc1_morte_frames
        self.hp = 2
        self.dano = 10
        self.tipo = "orc1"
        self.seguir = 300
        super().__init__(x, y)

class Orc2Enemy(OrcBase):
    def __init__(self, x, y):
        self.velocidade = 4
        self.machucado_frames = orc2_machucado_frames
        self.andando_frames = orc2_corpo_frames
        self.ataque_frames = orc2_ataque_frames
        self.morte_frames = orc2_morte_frames
        self.hp = 1
        self.dano = 8
        self.tipo = "orc2"
        self.seguir = 300
        super().__init__(x, y)

    def na_morte(self):
        return itemdropado(self.x + 112, self.y + 112, "moeda")

class Orc3Enemy(OrcBase):
    def __init__(self, x, y):
        self.velocidade = 3
        self.machucado_frames = orc3_machucado_frames
        self.andando_frames = orc3_corpo_frames
        self.ataque_frames = orc3_ataque_frames
        self.morte_frames = orc3_morte_frames
        self.hp = 3
        self.dano = 12
        self.tipo = "orc3"
        self.seguir = 300
        super().__init__(x, y)

    def na_morte(self):
        return itemdropado(self.x + 96, self.y + 96, "barril")

class VampiroBoss(OrcBase):
    def __init__(self, x, y, andando_frames, ataque_frames, machucado_frames, morte_frames, level=1):
        self.andando_frames = andando_frames
        self.frames_ataque = ataque_frames
        self.frames_machucado = machucado_frames
        self.frames_de_morte = morte_frames
        self.hp = 30 + level * 10
        self.max_hp = self.hp
        self.dano = 20 + level * 5
        self.tipo = f"vampiro{level}"
        self.velocidade = 1 + level * 0.2
        super().__init__(x, y)
        self.level = level
        self.linhas_ataque_especial = []        
        self.fase_ataque_especial = 0
        self.tempo_do_ultimo_ataque = pygame.time.get_ticks()
        self.intervalo_ataque_especial = 500
        self.ataque_especial_cooldown = 8000 
        self.na_sequencia_de_ataque = False
        self.delay_depois_ataque = 2500
        self.timer_depois_ataque = 0
        self.timer_ataque_especial = pygame.time.get_ticks()
        self.bloqueio_especial = False
        self.bloqueio_depois_do_especial = 0
        self.duracao_depois_do_especial = 2500
        self.distancia_seguir = 150000
        
    def na_morte(self):
        return itemdropado(self.x + 112, self.y + 112, "moeda")



    def ataque_em_circulo(self, offset_angle=0):
        for angle in range(offset_angle, 360 + offset_angle, 30):
            direcao = pygame.math.Vector2(1, 0).rotate(angle)
            projetil = {
                'x': self.x + 128,
                'y': self.y + 128,
                'dx': direcao.x * 8,
                'dy': direcao.y * 8,
                'timer': pygame.time.get_ticks(),
                'damage': 10 + self.level * 5,
                'ignora_imunidade': True 
            }
            efeitos_especiais.append(projetil)

    def ataque_especial(self):
        now = pygame.time.get_ticks()

        if self.bloqueio_especial and now - self.bloqueio_depois_do_especial >= self.duracao_depois_do_especial:
            self.bloqueio_especial = False

        if self.na_sequencia_de_ataque:
            if self.fase_ataque_especial < 3 and now - self.tempo_do_ultimo_ataque >= self.intervalo_ataque_especial:
                offset = 0 if self.fase_ataque_especial % 2 == 0 else 15
                self.ataque_em_circulo(offset_angle=offset)
                self.tempo_do_ultimo_ataque = now
                self.fase_ataque_especial += 1

                if self.fase_ataque_especial == 3:
                    self.timer_depois_ataque = now
                    self.parado = True

                    self.bloqueio_especial = True
                    self.bloqueio_depois_do_especial = now


            elif self.fase_ataque_especial == 3 and now - self.timer_depois_ataque >= self.delay_depois_ataque:
                self.na_sequencia_de_ataque = False
                self.timer_ataque_especial = now
                self.parado = False

                self.bloqueio_especial = True
                self.bloqueio_depois_do_especial = now

        elif now - self.timer_ataque_especial >= self.ataque_especial_cooldown:
            self.fase_ataque_especial = 0
            self.na_sequencia_de_ataque = True
            self.tempo_do_ultimo_ataque = now


    def barra_vida(self, surface):
        largura_barra = 600
        bar_height = 25
        bar_x = tela_largura // 2 - largura_barra// 2
        bar_y = 20
        pygame.draw.rect(surface, (255, 255, 255), (bar_x - 2, bar_y - 2, largura_barra + 4, bar_height + 4))
        filled = int((self.hp / self.max_hp) * largura_barra)
        pygame.draw.rect(surface, (221, 160, 221), (bar_x, bar_y, filled, bar_height))
    
    def desenha_ataque_especial(self, surface):
        for line in self.linhas_ataque_especial:
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
                         vampiro1_andando_frames,
                         vampiro1_ataque_frames,
                         vampiro1_machucado_frames,
                         vampiro1_morte_frames,
                         level=1)

class Vampiro2Boss(VampiroBoss):
    def __init__(self, x, y):
        super().__init__(x, y,
                         vampiro2_andando_frames,
                         vampiro2_ataque_frames,
                         vampiro2_machucado_frames,
                         vampiro2_morte_frames,
                         level=2)


class Vampiro3Boss(VampiroBoss):
    def __init__(self, x, y):
        super().__init__(x, y,
                         vampiro3_andando_frames,
                         vampiro3_ataque_frames,
                         vampiro3_machucado_frames,
                         vampiro3_morte_frames,
                         level=3)

def gerar_orcs_em_faixas(qtd=3):
    orcs = []
    for _ in range(qtd):
        faixa = random.choice(faixas_x)
        x = faixa - 128
        y = random.randint(-600, -100)
        x = max(0, min(x, tela_largura - 256))

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

class estado_de_jogo:
    player_y_comeco = tela_altura - 150
    dinheiro_total = 0
    colisao_com_player = False
    HP = 350
    max_HP = 350
    game_start_tela = True
    game_tela = False
    sem_colisao = True
    velocidade_obstaculo = 2.4
    pontuacao = 0
    moedas_ganhas = 0
    flechas = 0
    tempo_inicial = 0
    dano_timer = 0
    onda = 1
    cooldown_onda = 3000
    onda_timer = 0
    timer_mensagem_onda = 0
    mostra_mensagem_onda = False
    arma = 'espada'
    velocidade_player = 5
    alcance_espada = 60
    atacando = False
    ataque_frame_index = 0
    ataque_timer = 0
    duracao_do_ataque = 500
    player_machucado = False
    player_machucado_timer = 0
    player_machucado_duracao = 500
    player_morto = False
    player_morto_timer = 0
    player_morto_duracao = 2000
    player_morto_frame_index = 0
    player_machucado_frame_index = 0
    player_machucado_frame_timer = 0
    player_machucado_frame_delay = 0.2
    hp_castelo = 2000
    hp_max_castelo = 2000
    imune_a_explosao = False