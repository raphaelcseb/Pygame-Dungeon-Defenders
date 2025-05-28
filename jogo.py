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

my_font = pygame.font.Font(direcao_relativa('fonte/8BIT WONDER.ttf'), 32)
my_font_start = pygame.font.Font(direcao_relativa('fonte/8BIT WONDER.ttf'), 20)
small_font = pygame.font.Font(direcao_relativa('fonte/8BIT WONDER.ttf'), 10)

tela_de_inicio = pygame.image.load(direcao_relativa('imagens/fundo.png'))
tela_de_inicio = pygame.transform.scale(tela_de_inicio, (tela_largura, tela_altura))
loja = pygame.image.load(direcao_relativa('imagens/loja.png'))
loja = pygame.transform.scale(loja, (tela_largura, tela_altura))
overlay_castelo = pygame.image.load(direcao_relativa('imagens/castle overlay.png')).convert_alpha()
overlay_castelo = pygame.transform.scale(overlay_castelo, (tela_largura, tela_altura))
imagem_de_fundo = pygame.image.load(direcao_relativa('imagens/game map.png'))
imagem_de_fundo = pygame.transform.scale(imagem_de_fundo, (tela_largura, tela_altura))

player_folha_sprites = pygame.image.load(direcao_relativa('animação/jogador/Sword_Walk_full.png'))
player_ataque_sprites = pygame.image.load(direcao_relativa('animação/jogador/Sword_attack_full.png'))
player_machucado_sprites = pygame.image.load(direcao_relativa('animação/jogador/Sword_Hurt_full.png'))
player_morto_sprites = pygame.image.load(direcao_relativa('animação/jogador/Sword_Death_full.png'))

flecha_cima = pygame.image.load(direcao_relativa('itens/flecha_cima.png')).convert_alpha()
flecha_cima = pygame.transform.scale(flecha_cima, (46, 70))

flecha_baixo = pygame.image.load(direcao_relativa('itens/flecha_baixo.png')).convert_alpha()
flecha_baixo = pygame.transform.scale(flecha_baixo, (46, 70))

flecha_esquerda = pygame.image.load(direcao_relativa('itens/flecha_esquerda.png')).convert_alpha()
flecha_esquerda = pygame.transform.scale(flecha_esquerda, (70, 46))

flecha_direita = pygame.image.load(direcao_relativa('itens/flecha_direita.png')).convert_alpha()
flecha_direita = pygame.transform.scale(flecha_direita, (70, 46))

orc1_machucado_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc1_hurt_full.png'))
orc1_ataque_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc1_attack_full.png'))
orc1_corpo_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc1_walk_full.png'))
orc1_morte_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc1_death_full.png'))

orc2_machucado_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc2_hurt_full.png'))
orc2_ataque_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc2_attack_full.png'))
orc2_corpo_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc2_walk_full.png'))
orc2_morte_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc2_death_full.png'))

orc3_machucado_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc3_hurt_full.png'))
orc3_ataque_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc3_attack_full.png'))
orc3_corpo_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc3_walk_full.png'))
orc3_morte_sprites = pygame.image.load(direcao_relativa('animação/inimigo/orc3_death_full.png'))

vampiro1_andando_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires1_Walk_full.png'))
vampiro1_ataque_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires1_Attack_full.png'))
vampiro1_machucado_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires1_Hurt_full.png'))
vampiro1_morte_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires1_Death_full.png'))

vampiro2_andando_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires2_Walk_full.png'))
vampiro2_ataque_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires2_Attack_full.png'))
vampiro2_machucado_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires2_Hurt_full.png'))
vampiro2_morte_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires2_Death_full.png'))

vampiro3_andando_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires3_Walk_full.png'))
vampiro3_ataque_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires3_Attack_full.png'))
vampiro3_machucado_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires3_Hurt_full.png'))
vampiro3_morte_sprites = pygame.image.load(direcao_relativa('animação/inimigo/Vampires3_Death_full.png'))

imagem_moeda = pygame.image.load(direcao_relativa('itens/coin.png'))
imagem_moeda = pygame.transform.scale(imagem_moeda, (32, 32))
imagem_barril = pygame.image.load(direcao_relativa('itens/barrel.png'))
imagem_barril = pygame.transform.scale(imagem_barril, (64, 64))


pygame.mixer.music.load('Sons\Overworld_Hyrule.mp3') #Música de fundo em loop 
pygame.mixer.music.play(loops=-1)

pygame.mixer.music.set_volume(0.4)
espada_som = pygame.mixer.Sound('Sons\sword_cut.mp3')
som_compra = pygame.mixer.Sound('Sons\purchase_sound.mp3')
hit_orc_som = pygame.mixer.Sound('Sons\orc_hit.mp3')
vampiro_hiss = pygame.mixer.Sound('Sons\hiss.mp3')
explosao_som = pygame.mixer.Sound('Sons\explosion.mp3')
boss_fight = pygame.mixer.Sound('Sons\Boss_fight_zelda.mp3')

def carrega_orc_frames(sheet, largura_frame=64, altura_frame=64, escala=4, linhas=4, colunas=6):
    direcoes = ['baixo', 'cima', 'esquerda', 'direita']
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
    direcoes = ['baixo', 'esquerda', 'direita', 'cima']
    sprites = {dir: [] for dir in direcoes}
    for y, dir in enumerate(direcoes):
        for x in range(3):
            frame = sheet.subsurface(pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height))
            scaled_frame = pygame.transform.scale(frame, (frame_width * scale, frame_height * scale))
            sprites[dir].append(scaled_frame)
    return sprites

player_sprites = carrega_player_sprites(player_folha_sprites, 64, 64, scale=4)


def carrega_ataque_frames(sheet, frame_width=64, frame_height=64, rows=4, cols=8, scale=4):
    direcoes = ['baixo', 'esquerda', 'direita', 'cima']
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
orc2_morte_frames = carrega_orc_frames(orc2_morte_sprites)

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
    def __init__(atributo, x, y, tipo_item,caindo=False):
        atributo.x = x
        atributo.y = y
        atributo.tipo = tipo_item
        atributo.spawn_tempo = pygame.time.get_ticks()
        atributo.piscar_timer = 0
        atributo.visivel = True
        atributo.vida = 2 if tipo_item == "barril" else 1
        atributo.invulneravel_ate = pygame.time.get_ticks() + 2000
        atributo.rect = pygame.Rect(x, y, 32, 32) if tipo_item == "moeda" else pygame.Rect(x, y, 64, 64)
        atributo.caindo = False
        atributo.velocidade_cair = 3
        atributo.parar_y = tela_altura - 200
        atributo.caindo = caindo

    def update(atributo):
        tempo_atual = pygame.time.get_ticks()
        tempo_de_vida = tempo_atual - atributo.spawn_tempo

        if atributo.tipo == "moeda" and atributo.caindo:
            atributo.y += atributo.velocidade_cair
            if atributo.y >= atributo.parar_y:
                atributo.y = atributo.parar_y
                atributo.caindo = False

        atributo.rect.topleft = (atributo.x, atributo.y)

        if atributo.tipo == "moeda":
            if tempo_de_vida > 9000:
                atributo.piscar_timer += pygame.time.get_ticks() - (atributo.spawn_tempo + 3000)
                if atributo.piscar_timer > 200:
                    atributo.visivel = not atributo.visivel
                    atributo.piscar_timer = 0
            return tempo_de_vida < 11000

        elif atributo.tipo == "barril":
            return True

    
    def leva_dano(atributo):
        if pygame.time.get_ticks() < atributo.invulneravel_ate:
            return False
        atributo.vida -= 1
        atributo.invulneravel_ate = pygame.time.get_ticks() + 300  
        return atributo.vida <= 0


    def draw(proprio, superficie, show_hitbox=False):
        if not proprio.visivel and proprio.tipo == "moeda":
            return

        if proprio.tipo == "moeda":
            superficie.blit(imagem_moeda, proprio.rect.topleft)
        elif proprio.tipo == "barril":
            superficie.blit(imagem_barril, proprio.rect.topleft)

        if show_hitbox:
            pygame.draw.rect(superficie, (0, 255, 0), proprio.rect, 2)

class OrcBase:
    def __init__(atributo, x, y):
        atributo.x = x
        atributo.y = y
        atributo.frame_index = 0
        atributo.frame_atual = atributo.andando_frames
        atributo.frame_delay = 0.3
        atributo.frame_timer = 0
        atributo.parado = False
        atributo.atacando = False
        atributo.machucado = False
        atributo.machucado_timer = 0
        atributo.machucado_duracao = 500
        atributo.morto = False
        atributo.morto_timer = 0
        atributo.morto_duracao = 1000
        atributo.animacao_de_morte = False
        atributo.direcao = 'baixo'
        atributo.ultimo_ataque_castelo = 0
        atributo.intervalo_ataque_castelo = 1000
        atributo.hit_orc_som = hit_orc_som


    def update(atributo, dt, player_pos):
        if atributo.morto:
            atributo.frame_timer += dt
            if atributo.frame_timer >= atributo.frame_delay:
                direcao_frames = atributo.frame_atual.get(atributo.direcao, list(atributo.frame_atual.values())[0])
                if direcao_frames and atributo.frame_index < len(direcao_frames) - 1:
                    atributo.frame_index += 1
                    atributo.frame_timer = 0
                else:
                    atributo.animacao_de_morte = True
            return

        if getattr(atributo, "post_special_block", False):
            return

        if atributo.machucado:
            if pygame.time.get_ticks() - atributo.machucado_timer > atributo.machucado_duracao:
                atributo.machucado = False
                atributo.set_animacao("andar")

        if not atributo.parado:
            player_x, player_y = player_pos
            dist_x = player_x - atributo.x
            dist_y = player_y - atributo.y
            distancia = (dist_x**2 + dist_y**2) ** 0.5

            if distancia < atributo.seguir:
                norm_x = dist_x / distancia
                norm_y = dist_y / distancia
                atributo.x += norm_x * atributo.velocidade
                atributo.y += norm_y * atributo.velocidade

                if abs(dist_y) > abs(dist_x):
                    atributo.direcao = 'baixo' if dist_y > 0 else 'cima'
                else:
                    atributo.direcao = 'direita' if dist_x > 0 else 'esquerda'
            else:
                atributo.y += atributo.velocidade
                atributo.direcao = 'baixo'

            if atributo.y > tela_altura - 325:
                atributo.y = tela_altura - 325
                agora = pygame.time.get_ticks()
                if not atributo.parado:
                    atributo.set_animacao("atacar")
                    atributo.parado = True

                if agora - atributo.ultimo_ataque_castelo >= atributo.intervalo_ataque_castelo:
                    estado_de_jogo.hp_castelo -= atributo.dano
                    atributo.ultimo_ataque_castelo = agora

                    if estado_de_jogo.hp_castelo <= 0:
                        estado_de_jogo.player_morto = True
                        estado_de_jogo.player_morto_timer = pygame.time.get_ticks()

        atributo.frame_timer += dt
        if atributo.frame_timer >= atributo.frame_delay:
            direcao_frames = atributo.frame_atual.get(atributo.direcao, list(atributo.frame_atual.values())[0])
            if direcao_frames:
                atributo.frame_index = (atributo.frame_index + 1) % len(direcao_frames)
                atributo.frame_timer = 0

    def draw(atributo, superficie, show_hitbox=False):
        frame_list = atributo.frame_atual.get(atributo.direcao) or list(atributo.frame_atual.values())[0]
        if not frame_list:
            debug_frame = pygame.Surface((128, 128))
            debug_frame.fill((255, 0, 0))
            superficie.blit(debug_frame, (atributo.x, atributo.y))
            if show_hitbox:
                rect = pygame.Rect(atributo.x + 64, atributo.y + 64, 128, 128)
                pygame.draw.rect(superficie, (0, 255, 0), rect, 2)
            return
        frame_index = min(int(atributo.frame_index), len(frame_list) - 1)
        frame = frame_list[frame_index]

        if atributo.machucado and not atributo.morto:
            temp_superficie = pygame.Surface((frame.get_width(), frame.get_height()), pygame.SRCALPHA)
            temp_superficie.blit(frame, (0, 0))
            temp_superficie.fill((255, 0, 0, 100), special_flags=pygame.BLEND_MULT)
            superficie.blit(temp_superficie, (atributo.x, atributo.y))
        else:
            superficie.blit(frame, (atributo.x, atributo.y))

        if show_hitbox:
            rect = pygame.Rect(atributo.x + 64, atributo.y + 64, 128, 128)
            pygame.draw.rect(superficie, (0, 255, 0), rect, 2)

    def set_animacao(atributo, tipo):
        if atributo.morto:
            return

        if tipo == "andar":
            atributo.frame_atual = atributo.andando_frames
        elif tipo == "atacar":
            atributo.frame_atual = atributo.frames_ataque
            atributo.hit_orc_som.play()
        elif tipo == "hurt":
            atributo.frame_atual = atributo.frames_machucado
            atributo.machucado = True
            atributo.machucado_timer = pygame.time.get_ticks()
        elif tipo == "morrer":
            atributo.frame_atual = atributo.frames_de_morte
            atributo.morto = True
            atributo.frame_index = 0
            atributo.morto_timer = pygame.time.get_ticks()


class Orc1Enemy(OrcBase):
    def __init__(atributo, x, y):
        atributo.velocidade = 2
        atributo.frames_machucado = orc1_machucado_frames
        atributo.andando_frames = orc1_corpo_frames
        atributo.frames_ataque = orc1_ataque_frames
        atributo.frames_de_morte = orc1_morte_frames
        atributo.hp = 2
        atributo.dano = 10
        atributo.tipo = "orc1"
        atributo.seguir = 300
        super().__init__(x, y)

class Orc2Enemy(OrcBase):
    def __init__(atributo, x, y):
        atributo.velocidade = 3
        atributo.frames_machucado = orc2_machucado_frames
        atributo.andando_frames = orc2_corpo_frames
        atributo.frames_ataque = orc2_ataque_frames
        atributo.frames_de_morte = orc2_morte_frames
        atributo.hp = 1
        atributo.dano = 8
        atributo.tipo = "orc2"
        atributo.seguir = 300
        super().__init__(x, y)

    def ao_morrer(atributo):
        return itemdropado(atributo.x + 112, atributo.y + 112, "moeda")

class Orc3Enemy(OrcBase):
    def __init__(atributo, x, y):
        atributo.velocidade = 1
        atributo.frames_machucado = orc3_machucado_frames
        atributo.andando_frames = orc3_corpo_frames
        atributo.frames_ataque = orc3_ataque_frames
        atributo.frames_de_morte = orc3_morte_frames
        atributo.hp = 3
        atributo.dano = 12
        atributo.tipo = "orc3"
        atributo.seguir = 300
        super().__init__(x, y)

    def ao_morrer(atributo):
        return itemdropado(atributo.x + 96, atributo.y + 96, "barril")

class VampiroBoss(OrcBase):
    def __init__(atributo, x, y, andando_frames, ataque_frames, machucado_frames, morte_frames, level=1):
        atributo.andando_frames = andando_frames
        atributo.frames_ataque = ataque_frames
        atributo.frames_machucado = machucado_frames
        atributo.frames_de_morte = morte_frames
        atributo.hp = 30 + level * 10
        atributo.max_hp = atributo.hp
        atributo.dano = 20 + level * 5
        atributo.tipo = f"vampiro{level}"
        atributo.velocidade = 1 + level * 0.2
        super().__init__(x, y)
        atributo.level = level
        atributo.linhas_ataque_especial = []        
        atributo.fase_ataque_especial = 0
        atributo.tempo_do_ultimo_ataque = pygame.time.get_ticks()
        atributo.intervalo_ataque_especial = 500
        atributo.ataque_especial_cooldown = 8000 
        atributo.na_sequencia_de_ataque = False
        atributo.delay_depois_ataque = 2500
        atributo.timer_depois_ataque = 0
        atributo.timer_ataque_especial = pygame.time.get_ticks()
        atributo.bloqueio_especial = False
        atributo.bloqueio_depois_do_especial = 0
        atributo.duracao_depois_do_especial = 2500
        atributo.seguir = 150000
        
    def ao_morrer(atributo):
        return itemdropado(atributo.x + 112, atributo.y + 112, "moeda")



    def ataque_em_circulo(atributo, angulos=0):
        for angulo in range(angulos, 360 + angulos, 30):
            direcao = pygame.math.Vector2(1, 0).rotate(angulo)
            projetil = {
                'x': atributo.x + 128,
                'y': atributo.y + 128,
                'dx': direcao.x * 8,
                'dy': direcao.y * 8,
                'timer': pygame.time.get_ticks(),
                'dano': 10 + atributo.level * 5,
                'ignora_imunidade': True 
            }
            efeitos_especiais.append(projetil)

    def ataque_especial(atributos):
        now = pygame.time.get_ticks()

        if atributos.bloqueio_especial and now - atributos.bloqueio_depois_do_especial >= atributos.duracao_depois_do_especial:
            atributos.bloqueio_especial = False

        if atributos.na_sequencia_de_ataque:
            if atributos.fase_ataque_especial < 3 and now - atributos.tempo_do_ultimo_ataque >= atributos.intervalo_ataque_especial:
                offset = 0 if atributos.fase_ataque_especial % 2 == 0 else 15
                atributos.ataque_em_circulo(angulos=offset)
                atributos.tempo_do_ultimo_ataque = now
                atributos.fase_ataque_especial += 1

                if atributos.fase_ataque_especial == 3:
                    atributos.timer_depois_ataque = now
                    atributos.parado = True

                    atributos.bloqueio_especial = True
                    atributos.bloqueio_depois_do_especial = now


            elif atributos.fase_ataque_especial == 3 and now - atributos.timer_depois_ataque >= atributos.delay_depois_ataque:
                atributos.na_sequencia_de_ataque = False
                atributos.timer_ataque_especial = now
                atributos.parado = False

                atributos.bloqueio_especial = True
                atributos.bloqueio_depois_do_especial = now

        elif now - atributos.timer_ataque_especial >= atributos.ataque_especial_cooldown:
            atributos.fase_ataque_especial = 0
            atributos.na_sequencia_de_ataque = True
            atributos.tempo_do_ultimo_ataque = now


    def barra_vida(atributo, superficie):
        largura_barra = 600
        bar_height = 25
        bar_x = tela_largura // 2 - largura_barra// 2
        bar_y = 20
        pygame.draw.rect(superficie, (255, 255, 255), (bar_x - 2, bar_y - 2, largura_barra + 4, bar_height + 4))
        filled = int((atributo.hp / atributo.max_hp) * largura_barra)
        pygame.draw.rect(superficie, (221, 160, 221), (bar_x, bar_y, filled, bar_height))
    
    def desenha_ataque_especial(atributo, superficie):
        for linha in atributo.linhas_ataque_especial:
            pygame.draw.line(
                superficie, 
                (255, 0, 0),
                (linha['start_x'], linha['start_y']),
                (linha['end_x'], linha['end_y']),
                3
            )

class Vampiro1Boss(VampiroBoss):
    def __init__(atributo, x, y):
        super().__init__(x, y,
                         vampiro1_andando_frames,
                         vampiro1_ataque_frames,
                         vampiro1_machucado_frames,
                         vampiro1_morte_frames,
                         level=1)

class Vampiro2Boss(VampiroBoss):
    def __init__(atributo, x, y):
        super().__init__(x, y,
                         vampiro2_andando_frames,
                         vampiro2_ataque_frames,
                         vampiro2_machucado_frames,
                         vampiro2_morte_frames,
                         level=2)


class Vampiro3Boss(VampiroBoss):
    def __init__(atributo, x, y):
        super().__init__(x, y,
                         vampiro3_andando_frames,
                         vampiro3_ataque_frames,
                         vampiro3_machucado_frames,
                         vampiro3_morte_frames,
                         level=3)

def gerar_orcs_em_faixas(qtd=3):
    orcs = []
    faixa = random.choice(faixas_x)
    x = faixa - 128
    y = random.randint(-600, -100)
    x = max(0, min(x, tela_largura - 256))
    orcs.append(Orc3Enemy(x, y))

    for _ in range(qtd - 1):
        faixa = random.choice(faixas_x)
        x = faixa - 128
        y = random.randint(-600, -100)
        x = max(0, min(x, tela_largura - 256))

        tipo_orc = random.choices(['orc1', 'orc2', 'orc3'], weights=[0.4, 0.3, 0.3], k=1)[0]

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

def vida_castelo(superficie):
    largura_barra = 600
    altura_barra = 25
    barra_x = tela_largura // 2 - largura_barra // 2
    barra_y = tela_altura - 35

    pygame.draw.rect(superficie, (255, 255, 255), (barra_x - 2, barra_y - 2, largura_barra + 4, altura_barra + 4))
    
    filled = int((estado_de_jogo.hp_castelo / estado_de_jogo.hp_max_castelo) * largura_barra)
    pygame.draw.rect(superficie, (200, 0, 0), (barra_x, barra_y, filled, altura_barra))

tiros = []
itens_dropados = []
explosoes = []
efeitos_especiais = []
moedas_ceu = []

def HUD(superficie):
    hp_porcentagem = min(estado_de_jogo.HP / estado_de_jogo.max_HP, 1.0)
    hp_largura_barra = int(300 * hp_porcentagem)

    borda_barra_hp = pygame.Rect(18, 18, 304, 34)
    pygame.draw.rect(superficie, (255, 255, 255), borda_barra_hp)
    barra_hp = pygame.Rect(20, 20, hp_largura_barra, 30)
    pygame.draw.rect(superficie, (255, 0, 0), barra_hp)

    hud_fonte = pygame.font.Font(direcao_relativa('fonte/8BIT WONDER.ttf'), 24)
    texto_dinheiro = hud_fonte.render(f"Moedas* {estado_de_jogo.moedas_ganhas}", True, (255, 255, 0))
    texto_flechas = hud_fonte.render(f"Flechas* {estado_de_jogo.flechas}", True, (255, 255, 255))
    texto_armas = hud_fonte.render(f"Arma* {estado_de_jogo.arma.upper()}", True, (255, 255, 255))
    texto_wave = hud_fonte.render(f"Onda* {estado_de_jogo.onda}", True, (255, 255, 255))

    superficie.blit(texto_dinheiro, (20, 60))
    superficie.blit(texto_flechas, (20, 90))
    superficie.blit(texto_armas, (20, 120))
    superficie.blit(texto_wave, (20, 150))

def game_over_tela():
    tela.fill((0, 0, 0))
    fonte = pygame.font.Font(direcao_relativa('fonte/8BIT WONDER.ttf'), 60)
    fonte_pequena = pygame.font.Font(direcao_relativa('fonte/8BIT WONDER.ttf'), 30)

    texto_game_over = fonte.render("GAME OVER", True, (255, 0, 0))
    texto_moedas = fonte_pequena.render(f"Moedas coletadas* {estado_de_jogo.moedas_ganhas}", True, (255, 255, 255))
    texto_restart = fonte_pequena.render("Pressione R para reiniciar ou ESC para sair", True, (255, 255, 255))

    tela.blit(texto_game_over, (tela_largura // 2 - texto_game_over.get_width() // 2, tela_altura // 2 - 100))
    tela.blit(texto_moedas, (tela_largura // 2 - texto_moedas.get_width() // 2, tela_altura // 2))
    tela.blit(texto_restart, (tela_largura // 2 - texto_restart.get_width() // 2, tela_altura // 2 + 60))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False
                    estado_de_jogo.game_start_tela = False

                    tiros.clear()
                    itens_dropados.clear()
                    explosoes.clear()
                    moedas_ceu.clear()
                    efeitos_especiais.clear()

                    estado_de_jogo.player_morto = False
                    estado_de_jogo.HP = estado_de_jogo.max_HP
                    estado_de_jogo.dano_timer = 0
                    estado_de_jogo.player_morto_timer = 0
                    estado_de_jogo.player_morto_frame_index = 0
                    estado_de_jogo.moedas_ganhas = 0
                    estado_de_jogo.flechas = 0
                    estado_de_jogo.onda = 1
                    estado_de_jogo.hp_castelo = estado_de_jogo.hp_max_castelo
                    estado_de_jogo.atacando = False

                    game()

def game():
    ultimo_spawn_moeda_ceu = pygame.time.get_ticks()
    intervalo_moeda_ceu = 10000 
    estado_de_jogo.imune_a_explosao = False
    dano_intervalo = 100
    cooldown_ataque = 500
    ultimo_ataque = 0
    relogio = pygame.time.Clock()
    funcionando = True
    player_largura = 128
    player_altura = 128
    player_x = tela_largura // 2
    player_y = tela_altura // 2
    player_hitbox = pygame.Rect(player_x, player_y, player_largura, player_altura)
    centro_x = player_hitbox.centerx
    centro_y = player_hitbox.centery
    player_dir = 'baixo'
    player_frame_index = 0
    player_frame_timer = 0
    frame_delay = 0.15
    raio_aura = 80
    ultimo_tiro = 0
    cooldown_tiro = 500

    orcs = gerar_orcs_em_faixas(5)

    estado_de_jogo.HP = estado_de_jogo.max_HP
    estado_de_jogo.flechas = 0
    estado_de_jogo.moedas_ganhas = 0
    estado_de_jogo.pontuacao = 0
    estado_de_jogo.arma = 'espada'
    estado_de_jogo.velocidade_player = 5

    while funcionando:
        if estado_de_jogo.onda == 3 or estado_de_jogo.onda == 6 or estado_de_jogo.onda == 9:
            pygame.mixer.music.fadeout(1000)
            boss_fight.play(loops=-1)
        elif estado_de_jogo.onda == 4 or estado_de_jogo.onda == 7:
            pygame.mixer.music.play()
        if estado_de_jogo.player_morto:
            if pygame.time.get_ticks() - estado_de_jogo.player_morto_timer >= estado_de_jogo.player_morto_duracao:
                game_over_tela()
                return
            else:
                dt = relogio.tick(60) / 1000
                tela.blit(imagem_de_fundo, (0, 0))
                frame = player_frames_morte[player_dir][estado_de_jogo.player_morto_frame_index]
                if estado_de_jogo.imune_a_explosao:
                    raio_aura = 80
                    aura_superficie = pygame.Surface((raio_aura * 2, raio_aura * 2), pygame.SRCALPHA)
                    pygame.draw.circle(aura_superficie, (255, 255, 0, 40), (raio_aura, raio_aura), raio_aura - 5)
                    tela.blit(aura_superficie, (centro_x - raio_aura, centro_y - raio_aura))

                HUD(tela)
                pygame.display.flip()
                continue

        dt = relogio.tick(60) / 1000
        if pygame.time.get_ticks() - ultimo_spawn_moeda_ceu > intervalo_moeda_ceu:
            nasce_moeda_ceu()
            ultimo_spawn_moeda_ceu = pygame.time.get_ticks()

        tela.blit(imagem_de_fundo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    funcionando = False
                elif event.key == pygame.K_1:
                    estado_de_jogo.arma = 'espada'
                elif event.key == pygame.K_2:
                    estado_de_jogo.arma = 'arco'
                elif event.key == pygame.K_SPACE:
                    tempo_atual = pygame.time.get_ticks()
                    if estado_de_jogo.arma == 'espada' and tempo_atual - ultimo_ataque >= cooldown_ataque:
                        ultimo_ataque = tempo_atual

                        player_center_x = player_hitbox.centerx
                        player_center_y = player_hitbox.centery
                        largura_ataque = estado_de_jogo.alcance_espada
                        altura_ataque = 80 + estado_de_jogo.alcance_espada

                        if player_dir == 'cima':
                            ataque_rect = pygame.Rect(
                                player_center_x - largura_ataque // 2,
                                player_center_y - altura_ataque,
                                largura_ataque,
                                altura_ataque
                            )
                            pygame.draw.rect(tela, (255, 255, 0), ataque_rect, 2)
                            estado_de_jogo.atacando = True
                            estado_de_jogo.ataque_timer = pygame.time.get_ticks()
                            estado_de_jogo.ataque_frame_index = 0

                        elif player_dir == 'baixo':
                            ataque_rect = pygame.Rect(
                                player_center_x - largura_ataque // 2,
                                player_center_y,
                                largura_ataque,
                                altura_ataque
                            )
                            pygame.draw.rect(tela, (255, 255, 0), ataque_rect, 2)
                            estado_de_jogo.atacando = True
                            estado_de_jogo.ataque_timer = pygame.time.get_ticks()
                            estado_de_jogo.ataque_frame_index = 0

                        elif player_dir == 'esquerda':
                            ataque_rect = pygame.Rect(
                                player_center_x - altura_ataque,
                                player_center_y - largura_ataque // 2,
                                altura_ataque,
                                largura_ataque
                            )
                            pygame.draw.rect(tela, (255, 255, 0), ataque_rect, 2)
                            estado_de_jogo.atacando = True
                            estado_de_jogo.ataque_timer = pygame.time.get_ticks()
                            estado_de_jogo.ataque_frame_index = 0

                        elif player_dir == 'direita':
                            ataque_rect = pygame.Rect(
                                player_center_x,
                                player_center_y - largura_ataque // 2,
                                altura_ataque,
                                largura_ataque
                            )
                            pygame.draw.rect(tela, (255, 255, 0), ataque_rect, 2)
                            estado_de_jogo.atacando = True
                            estado_de_jogo.ataque_timer = pygame.time.get_ticks()
                            estado_de_jogo.ataque_frame_index = 0

                        for orc in orcs[:]:
                            if orc.morto:
                                continue
                            orc_rect = pygame.Rect(orc.x + 64, orc.y + 64, 128, 128)
                            if ataque_rect.colliderect(orc_rect):
                                orc.hp -= 1
                                if orc.hp <= 0:
                                    orc.set_animacao("morrer")
                                    if hasattr(orc, "ao_morrer"):
                                        itens_dropados.append(orc.ao_morrer())
                                    estado_de_jogo.moedas_ganhas += 1
                                else:
                                    orc.set_animacao("hurt")

                        for item in itens_dropados[:]:
                            if item.tipo == "barril" and ataque_rect.colliderect(item.rect):
                                if item.leva_dano():
                                    cria_explosao(item.x + 32, item.y + 32, 150, 25)
                                    itens_dropados.remove(item)
                                break

                    elif estado_de_jogo.arma == 'arco' and estado_de_jogo.flechas > 0:
                        tempo_atual = pygame.time.get_ticks()
                        if tempo_atual - ultimo_tiro >= cooldown_tiro:
                            imagem_tiro = {
                                'cima': flecha_cima,
                                'baixo': flecha_baixo,
                                'esquerda': flecha_esquerda,
                                'direita': flecha_direita
                            }[player_dir]

                            centro_x_tiro = player_hitbox.centerx
                            centro_y_tiro = player_hitbox.centery

                            if player_dir == 'cima':
                                tiro_x = centro_x_tiro - flecha_cima.get_width() // 2
                                tiro_y = centro_y_tiro - flecha_cima.get_height()
                                tiro_img = flecha_cima
                            elif player_dir == 'baixo':
                                tiro_x = centro_x_tiro - flecha_baixo.get_width() // 2
                                tiro_y = centro_y_tiro
                                tiro_img = flecha_baixo
                            elif player_dir == 'esquerda':
                                tiro_x = centro_x_tiro - flecha_esquerda.get_width()
                                tiro_y = centro_y_tiro - flecha_esquerda.get_height() // 2
                                tiro_img = flecha_esquerda
                            elif player_dir == 'direita':
                                tiro_x = centro_x_tiro
                                tiro_y = centro_y_tiro - flecha_direita.get_height() // 2
                                tiro_img = flecha_direita

                            balas = {
                                'x': tiro_x,
                                'y': tiro_y,
                                'velocidade': 10,
                                'dir': player_dir,
                                'img': tiro_img
                            }
                            tiros.append(balas)
                            estado_de_jogo.flechas -= 1
                            ultimo_tiro = tempo_atual

        jogador_movendo = False
        tecla = pygame.key.get_pressed()
        if (tecla[pygame.K_LEFT] or tecla[pygame.K_a]) and player_x > 0:
            player_x -= estado_de_jogo.velocidade_player
            player_dir = 'esquerda'
            jogador_movendo = True

        if (tecla[pygame.K_RIGHT] or tecla[pygame.K_d]) and player_x < tela_largura - 128:
            player_x += estado_de_jogo.velocidade_player
            player_dir = 'direita'
            jogador_movendo = True

        if (tecla[pygame.K_UP] or tecla[pygame.K_w]) and player_y > -90:
            player_y -= estado_de_jogo.velocidade_player
            player_dir = 'cima'
            jogador_movendo = True

        limite_y_orc = tela_altura - 280
        if (tecla[pygame.K_DOWN] or tecla[pygame.K_s]) and player_y < limite_y_orc:
            player_y += estado_de_jogo.velocidade_player
            player_dir = 'baixo'
            jogador_movendo = True


        hitbox_largura = 64
        hitbox_altura = 80
        player_hitbox = pygame.Rect(
            player_x + (128 - hitbox_largura) // 2,
            player_y + (128 - hitbox_altura),
            hitbox_largura,
            hitbox_altura)
        centro_x = player_hitbox.centerx
        centro_y = player_hitbox.centery

        for item in itens_dropados[:]:
            if item.tipo == "moeda":
                if not item.update():
                    itens_dropados.remove(item)
                    continue
                if player_hitbox.colliderect(item.rect):
                    itens_dropados.remove(item)
                    estado_de_jogo.moedas_ganhas += 1
                    continue
            item.draw(tela, show_hitbox=True)

        for moeda_do_ceu in moedas_ceu[:]:
            if not moeda_do_ceu.update():
                moedas_ceu.remove(moeda_do_ceu)
                continue
            if player_hitbox.colliderect(moeda_do_ceu.rect):
                moedas_ceu.remove(moeda_do_ceu)
                estado_de_jogo.moedas_ganhas += 1
                continue
            moeda_do_ceu.draw(tela, show_hitbox=True)

        for orc in sorted(orcs, key=lambda o: o.y):
            if orc.morto:

                orc.update(dt, (player_x, player_y))
                continue

            if isinstance(orc, VampiroBoss) and orc.bloqueio_especial:
                orc.update(dt, (player_x, player_y))
                continue

            orc_rect = pygame.Rect(orc.x + 64, orc.y + 64, 128, 128)
            if player_hitbox.colliderect(orc_rect):
                agora = pygame.time.get_ticks()
                if agora - estado_de_jogo.dano_timer >= dano_intervalo and not estado_de_jogo.player_machucado and not estado_de_jogo.player_morto:
                    estado_de_jogo.HP -= orc.dano
                    estado_de_jogo.dano_timer = agora
                    estado_de_jogo.player_machucado = True
                    estado_de_jogo.player_machucado_timer = agora
                    estado_de_jogo.player_machucado_frame_index = 0
                    estado_de_jogo.player_machucado_frame_timer = 0
                    if estado_de_jogo.HP <= 0:
                        estado_de_jogo.player_morto = True

                orc.parado = True
                orc.set_animacao("atacar")
            else:
                orc.parado = False
                orc.set_animacao("andar")

            orc.update(dt, (player_x, player_y))

        orcs = [orc for orc in orcs if not orc.animacao_de_morte]

        if estado_de_jogo.player_morto:
            tempo_passado = pygame.time.get_ticks() - estado_de_jogo.player_morto_timer
            progesso = tempo_passado / estado_de_jogo.player_morto_duracao
            estado_de_jogo.player_morto_frame_index = min(
                int(progesso * len(player_frames_morte[player_dir])),
                len(player_frames_morte[player_dir]) - 1)
            frame = player_frames_morte[player_dir][estado_de_jogo.player_morto_frame_index]

        elif estado_de_jogo.player_machucado:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - estado_de_jogo.player_machucado_timer >= estado_de_jogo.player_machucado_duracao:
                estado_de_jogo.player_machucado = False
                estado_de_jogo.player_machucado_frame_index = 0
                estado_de_jogo.player_machucado_frame_timer = 0
                frame = player_sprites[player_dir][player_frame_index]
            else:
                estado_de_jogo.player_machucado_frame_timer += dt
                if estado_de_jogo.player_machucado_frame_timer >= estado_de_jogo.player_machucado_frame_delay:
                    estado_de_jogo.player_machucado_frame_index = (
                        estado_de_jogo.player_machucado_frame_index + 1
                    ) % len(player_machucado_frames[player_dir])
                    estado_de_jogo.player_machucado_frame_timer = 0
                frame = player_machucado_frames[player_dir][estado_de_jogo.player_machucado_frame_index]

        elif estado_de_jogo.atacando:
            tempo_atual = pygame.time.get_ticks()
            progesso = (tempo_atual - estado_de_jogo.ataque_timer) / estado_de_jogo.duracao_do_ataque
            lista_frames = player_ataque_frames[player_dir]
            estado_de_jogo.ataque_frame_index = min(int(progesso * len(lista_frames)), len(lista_frames) - 1)
            frame = lista_frames[estado_de_jogo.ataque_frame_index]

            if tempo_atual - estado_de_jogo.ataque_timer >= estado_de_jogo.duracao_do_ataque:
                estado_de_jogo.atacando = False

        else:
            frame = player_sprites[player_dir][player_frame_index]

        desenhaveis = []

        for orc in orcs:
            desenhaveis.append({'y': orc.y, 'type': 'orc', 'obj': orc})

        desenhaveis.append({'y': player_y, 'type': 'player', 'obj': frame})

        for balas in tiros:
            tela.blit(balas['img'], (balas['x'], balas['y']))

        for entidade in sorted(desenhaveis, key=lambda e: e['y']):
            if entidade['type'] == 'orc':
                entidade['obj'].draw(tela, show_hitbox=True)
            elif entidade['type'] == 'player':
                tela.blit(entidade['obj'], (player_x - 60, player_y - 40))

        for explosion in explosoes[:]:
            tempo_atual = pygame.time.get_ticks()
            progesso = (tempo_atual - explosion['timer']) / explosion['duration']
            if progesso >= 1:
                explosoes.remove(explosion)
                continue

            explosao_rect = pygame.Rect(
                explosion['x'] - explosion['radius'],
                explosion['y'] - explosion['radius'],
                explosion['radius'] * 2,
                explosion['radius'] * 2)

            for orc in orcs[:]:
                if orc.morto:
                    continue
                orc_center = pygame.Rect(orc.x + 96, orc.y + 96, 1, 1)
                if orc_center.colliderect(explosao_rect):
                    orc.hp -= explosion['dano']
                    if orc.hp <= 0:
                        orc.set_animacao("morrer")
                        if hasattr(orc, "ao_morrer"):
                            itens_dropados.append(orc.ao_morrer())
                        estado_de_jogo.moedas_ganhas += 1
                    else:
                        orc.set_animacao("hurt")

            player_center = pygame.Rect(player_x + 96, player_y + 96, 1, 1)
            if player_center.colliderect(explosao_rect) and not estado_de_jogo.imune_a_explosao:
                agora = pygame.time.get_ticks()
                if agora - estado_de_jogo.dano_timer >= dano_intervalo:
                    estado_de_jogo.HP -= explosion['dano']
                    estado_de_jogo.dano_timer = agora

            explosao_tempo_passado = pygame.time.get_ticks() - explosion['timer']
            alpha = max(0, min(255, 255 - int(255 * (explosao_tempo_passado / 1000))))
            superficie_explosao = pygame.Surface((explosion['radius'] * 2, explosion['radius'] * 2), pygame.SRCALPHA)
            pygame.draw.circle(
                superficie_explosao,
                (255, 165, 0, alpha),
                (explosion['radius'], explosion['radius']),
                int(explosion['radius'] * progesso)
            )
            tela.blit(superficie_explosao, (explosion['x'] - explosion['radius'], explosion['y'] - explosion['radius']))

        orcs = [orc for orc in orcs if not orc.animacao_de_morte]

        if not orcs:
            estado_de_jogo.onda_timer += dt * 1000  # Ajustar para milissegundos
            if estado_de_jogo.onda_timer >= estado_de_jogo.cooldown_onda:
                estado_de_jogo.onda += 1
                estado_de_jogo.onda_timer = 0
                estado_de_jogo.mostra_mensagem_onda = True
                estado_de_jogo.timer_mensagem_onda = pygame.time.get_ticks()

                mostra_loja()
                itens_dropados.clear()
                moedas_ceu.clear()
                efeitos_especiais.clear()
                tiros.clear()

                qtd_orcs = 5 + estado_de_jogo.onda
                if estado_de_jogo.onda in [3, 6, 10]:
                    if estado_de_jogo.onda == 3:
                        orcs = [Vampiro1Boss(tela_largura // 2 - 128, -300)]
                    elif estado_de_jogo.onda == 6:
                        orcs = [Vampiro2Boss(tela_largura // 2, -300)]
                    elif estado_de_jogo.onda == 10:
                        orcs = [Vampiro3Boss(tela_largura // 2, -400)]
                else:
                    novos_orcs = gerar_orcs_em_faixas(qtd_orcs)
                    if not novos_orcs:
                        novos_orcs = [Orc1Enemy(random.choice(faixas_x) - 128, -100),
                                      Orc2Enemy(random.choice(faixas_x) - 128, -100),
                                      Orc3Enemy(random.choice(faixas_x) - 128, -100)]
                    for orc in novos_orcs:
                        orc.velocidade += estado_de_jogo.onda * 0.05
                        orc.velocidade = min(orc.velocidade, 5.0)
                        if estado_de_jogo.onda >= 3:
                            if orc.tipo == "orc1":
                                orc.hp = min(3, orc.hp + estado_de_jogo.onda // 3)
                            elif orc.tipo == "orc2":
                                orc.hp = min(2, orc.hp + estado_de_jogo.onda // 4)
                            elif orc.tipo == "orc3":
                                orc.hp = min(4, orc.hp + estado_de_jogo.onda // 2)
                    orcs = novos_orcs

        atualiza_tiros(dt, orcs)

        if jogador_movendo:
            player_frame_timer += dt
            if player_frame_timer >= frame_delay:
                player_frame_index = (player_frame_index + 1) % 3
                player_frame_timer = 0
        else:
            player_frame_index = 1

        if estado_de_jogo.player_morto:
            tempo_passado = pygame.time.get_ticks() - estado_de_jogo.player_morto_timer
            progesso = tempo_passado / estado_de_jogo.player_morto_duracao
            estado_de_jogo.player_morto_frame_index = min(int(progesso * len(player_frames_morte[player_dir])),len(player_frames_morte[player_dir]) - 1)
            frame = player_frames_morte[player_dir][estado_de_jogo.player_morto_frame_index]

        elif estado_de_jogo.player_machucado:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - estado_de_jogo.player_machucado_timer >= estado_de_jogo.player_machucado_duracao:
                estado_de_jogo.player_machucado = False
                estado_de_jogo.player_machucado_frame_index = 0
                estado_de_jogo.player_machucado_frame_timer = 0
                frame = player_sprites[player_dir][player_frame_index]
            else:
                estado_de_jogo.player_machucado_frame_timer += dt
                if estado_de_jogo.player_machucado_frame_timer >= estado_de_jogo.player_machucado_frame_delay:
                    estado_de_jogo.player_machucado_frame_index = (estado_de_jogo.player_machucado_frame_index + 1) % len(player_machucado_frames[player_dir])
                    estado_de_jogo.player_machucado_frame_timer = 0
                frame = player_machucado_frames[player_dir][estado_de_jogo.player_machucado_frame_index]

        elif estado_de_jogo.atacando:
            tempo_atual = pygame.time.get_ticks()
            progesso = (tempo_atual - estado_de_jogo.ataque_timer) / estado_de_jogo.duracao_do_ataque
            lista_frames = player_ataque_frames[player_dir]
            estado_de_jogo.ataque_frame_index = min(int(progesso * len(lista_frames)), len(lista_frames) - 1)
            frame = lista_frames[estado_de_jogo.ataque_frame_index]

            if tempo_atual - estado_de_jogo.ataque_timer >= estado_de_jogo.duracao_do_ataque:
                estado_de_jogo.atacando = False

        else:
            frame = player_sprites[player_dir][player_frame_index]

        if estado_de_jogo.imune_a_explosao:
            raio_aura = 80
            aura_superficie = pygame.Surface((raio_aura * 2, raio_aura * 2), pygame.SRCALPHA)
            pygame.draw.circle(aura_superficie, (255, 255, 0, 40), (raio_aura, raio_aura), raio_aura - 5)
            tela.blit(aura_superficie, (centro_x - raio_aura, centro_y - raio_aura))

        pygame.draw.rect(tela, (255, 0, 0), player_hitbox, 2)

        HUD(tela)

        for orc in orcs:
            if isinstance(orc, VampiroBoss) and not orc.morto:
                orc.ataque_especial()
                orc.barra_vida(tela)

        player_rect = pygame.Rect(player_x + 48, player_y + 48, 128, 128)

        if estado_de_jogo.player_morto and pygame.time.get_ticks() - estado_de_jogo.player_morto_timer >= estado_de_jogo.player_morto_duracao:
            game_over_tela()
            return



        if estado_de_jogo.mostra_mensagem_onda:
            texto_onda = my_font.render(f"WAVE {estado_de_jogo.onda}", True, (255, 255, 255))
            tela.blit(texto_onda, (tela_largura // 2 - 80, 80))
            if pygame.time.get_ticks() - estado_de_jogo.timer_mensagem_onda > 2000:
                estado_de_jogo.mostra_mensagem_onda = False

        for efeito in efeitos_especiais[:]:
            if (efeito['x'] < 0 or efeito['x'] > tela_largura or
                efeito['y'] < 0 or efeito['y'] > tela_altura):
                efeitos_especiais.remove(efeito)
                continue

            tempo_passado = pygame.time.get_ticks() - efeito['timer']
            alpha = max(0, min(255, 255 - int(255 * (tempo_passado / 1000))))
            raio = min(480, max(1, 6 + (tempo_passado // 100)))

            superficie = pygame.Surface((raio, raio), pygame.SRCALPHA)
            pygame.draw.circle(superficie, (255, 0, 0, alpha), (raio, raio), raio*10)
            tela.blit(superficie, (efeito['x'], efeito['y']))

            efeito['x'] += efeito['dx']
            efeito['y'] += efeito['dy']

            player_rect = pygame.Rect(player_x + 48, player_y + 48, 64, 64)
            effect_rect = pygame.Rect(efeito['x'], efeito['y'], 12, 12)
            if effect_rect.colliderect(player_rect):
                ignora_imunidade = efeito.get('ignora_imunidade', False)
                if ignora_imunidade or not estado_de_jogo.imune_a_explosao:
                    now = pygame.time.get_ticks()
                    if now - estado_de_jogo.dano_timer >= 100:  # Reduzido de dano_intervalo (2000) para 100ms
                        estado_de_jogo.HP -= efeito['dano']
                        estado_de_jogo.dano_timer = now
                        estado_de_jogo.player_machucado = True
                        estado_de_jogo.player_machucado_timer = now
                        estado_de_jogo.player_machucado_frame_index = 0
                        estado_de_jogo.player_machucado_frame_timer = 0
                        if estado_de_jogo.HP <= 0:
                            estado_de_jogo.player_morto = True
                        # Não remover efeito aqui, permitindo múltiplos danos

            pygame.draw.circle(tela, (255, 0, 0), (int(efeito['x']), int(efeito['y'])), 6)
            pygame.draw.rect(tela, (0, 0, 255), pygame.Rect(efeito['x'], efeito['y'], 12, 12), 2)

        
        tela.blit(overlay_castelo, (0, tela_altura - overlay_castelo.get_height()))
        vida_castelo(tela)
        pygame.display.flip()

def cria_explosao(x, y, raio, dano):
    explosoes.append({'x': x,'y': y,'radius': raio * 1.5,'dano': dano,'timer': pygame.time.get_ticks(),'duration': 500})

def nasce_moeda_ceu():
    faixa = random.choice(faixas_x)
    x = faixa - 16
    y = -50 
    moeda = itemdropado(x, y, "moeda", caindo=True) 
    moeda.caindo = True
    moeda.spawn_tempo = pygame.time.get_ticks()
    moedas_ceu.append(moeda)

def atualiza_tiros(dt, orcs):
    global tiros
    for tiro in tiros[:]:
        if tiro['dir'] == 'cima':
            tiro['y'] -= tiro['velocidade']
        elif tiro['dir'] == 'baixo':
            tiro['y'] += tiro['velocidade']
        elif tiro['dir'] == 'esquerda':
            tiro['x'] -= tiro['velocidade']
        elif tiro['dir'] == 'direita':
            tiro['x'] += tiro['velocidade']

        bala_rect = pygame.Rect(tiro['x'], tiro['y'], 24, 12) if tiro['dir'] in ('esquerda', 'direita') else pygame.Rect(tiro['x'], tiro['y'], 12, 24)

        for orc in orcs[:]:
            orc_rect = pygame.Rect(orc.x + 64, orc.y + 64, 128, 128)
            if bala_rect.colliderect(orc_rect):
                if tiro in tiros:
                    tiros.remove(tiro)

                if not orc.morto:
                    orc.hp -= 2
                    if orc.hp <= 0:
                        orc.set_animacao("morrer")
                        if hasattr(orc, "ao_morer"):
                            itens_dropados.append(orc.ao_morrer())
                        estado_de_jogo.moedas_ganhas += 1
                    else:
                        orc.set_animacao("hurt")
                break


        for item in itens_dropados[:]:
            if item.tipo == "barril" and bala_rect.colliderect(item.rect):
                if item.leva_dano():
                    cria_explosao(item.x + 32, item.y + 32, 150, 25)
                    itens_dropados.remove(item)
                if tiro in tiros:
                    tiros.remove(tiro)
                break


        if (tiro['x'] < 0 or tiro['x'] > tela_largura or tiro['y'] < 0 or tiro['y'] > tela_altura):
            if tiro in tiros:
                tiros.remove(tiro)
            continue

def mostra_loja():
    loja_ativa = True
    opcoes = [
        {"name": "Aumentar Vida (+50)", "custo": 10, "acao": lambda: setattr(estado_de_jogo, 'HP', min(estado_de_jogo.max_HP, estado_de_jogo.HP + 50))},
        {"name": "Recuperar Vida", "custo": 5, "acao": lambda: setattr(estado_de_jogo, 'HP', estado_de_jogo.max_HP)},
        {"name": "Mais Flechas (+10)", "custo": 8, "acao": lambda: setattr(estado_de_jogo, 'flechas', estado_de_jogo.flechas + 10)},
        {"name": "Aumentar Velocidade", "custo": 15, "acao": lambda: setattr(estado_de_jogo, 'player_velocidade', estado_de_jogo.velocidade_player + 0.5)},
        {"name": "Aumentar Area da Espada", "custo": 12, "acao": lambda: setattr(estado_de_jogo, 'sword_range', estado_de_jogo.alcance_espada + 20)},
        {"name": "Reparar Castelo (+500)", "custo": 20, "acao": lambda: min(estado_de_jogo.hp_castelo + 500, estado_de_jogo.hp_max_castelo)}
    ]
    
    if not estado_de_jogo.imune_a_explosao:
        opcoes.append({
            "name": "Imunidade Permanente a Explosões", 
            "custo": 50, 
            "acao": lambda: [setattr(estado_de_jogo, 'imune_a_explosões', True)]})

    opcao_fonte = pygame.font.Font(direcao_relativa('fonte/8BIT WONDER.ttf'), 30)

    while loja_ativa:
        tela.blit(loja, (0, 0))
        moedas_texto = opcao_fonte.render(f"Moedas* {estado_de_jogo.moedas_ganhas}", True, (255, 255, 0))  # Amarelo
        tela.blit(moedas_texto, (tela_largura // 2 - moedas_texto.get_width() // 2 + 4, 210))
        pygame.display.flip()

        opcao_espaco = 40
        comeco_y = 150

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    loja_ativa = False
                elif evento.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7):
                    opcao_index = evento.key - pygame.K_1
                    if opcao_index < len(opcoes):
                        opcao = opcoes[opcao_index]
                        if estado_de_jogo.moedas_ganhas >= opcao['custo']:
                            estado_de_jogo.moedas_ganhas -= opcao['custo']
                            resultado = opcao['acao']()

                            texto_de_feedback = opcao_fonte.render(f"Comprado* {opcao['name']}", True, (0, 255, 0))
                            tela.blit(texto_de_feedback, (tela_largura // 2 - texto_de_feedback.get_width() // 2, comeco_y + len(opcoes)*opcao_espaco + 380))
                            pygame.display.flip()
                            pygame.time.delay(1500) 

                            if opcao['name'].startswith("Aumentar Vida"):
                                estado_de_jogo.HP = min(estado_de_jogo.max_HP, estado_de_jogo.HP + 50)
                            elif opcao['name'].startswith("Recuperar Vida"):
                                estado_de_jogo.HP = estado_de_jogo.max_HP
                            elif opcao['name'].startswith("Reparar Castelo"):
                                estado_de_jogo.hp_castelo = min(estado_de_jogo.hp_castelo + 500, estado_de_jogo.hp_max_castelo)

def start_tela():
    while estado_de_jogo.game_start_tela:
        tela.blit(tela_de_inicio, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    estado_de_jogo.game_start_tela = False
                    game()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

if __name__ == "__main__":
    start_tela()