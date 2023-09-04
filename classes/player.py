import pygame
from basic_game_config import screen_width, screen_height
from sounds import shooting_sound
from functions.collision import collision_check
from classes.bullet import Bullet
from classes.bg import Bg
from sprite_groups import *

background = Bg()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        for s in range(1, 5):
            self.sprites.append(pygame.image.load(
                f'Sprites/player/player_{s}.png').convert_alpha())
        self.sprite_index = 0
        self.image = self.sprites[self.sprite_index]
        self.rect = self.image.get_rect(
            center=(screen_width/2, screen_height - 80))
        self.bullet_count = 0
        self.auto_shooting = False
        self.count = 1
        self.player_speed = 8
        self.player_score = 0
        self.game_active = False
        self.game_time = 0
        self.score_add = 5
        self.shoot_timer = self.score_time = pygame.time.get_ticks()
        self.shoot_interval = 600
        self.shoot_interval_2 = 400
        self.shoot_interval_3 = 350
        self.countt = 0
        self.shooting = False
        self.score_count = 0

    def update(self):
        """A cada frame do jogo, incrementa 0.1 na variável 
        self.sprite_index, que quando chega a um valor inteiro, 
        o self.image é trocado pelo próximo sprite do player.
        Se self.sprite_index for maior que a quantidade de sprites
        ele é definido como 0."""
        self.score_count += 1
        self.sprite_index += 0.1
        if self.sprite_index > len(self.sprites):
            self.sprite_index = 0
        self.image = self.sprites[int(self.sprite_index)]

    def player_inputs(self, keys):
        """Checa inputs do jogador quando o jogo está ativo.
        Se 'd' for apertado, é incrementado self.player_speed 
        no eixo x do jogador. Se 'a' é apertado, é subtraido 
        self.player_speed do eixo x do jogador.
          """
        if keys[pygame.K_d]:
            self.rect.x += self.player_speed
            if self.rect.right >= screen_width:
                self.rect.right = screen_width
        if keys[pygame.K_a]:
            self.rect.x -= self.player_speed
            if self.rect.x <= 0:
                self.rect.x = 0

    def create_bullet(self):
        return Bullet(self.rect.midtop[0], self.rect.midtop[1])

    def auto_bullet(self):
        """Se self.auto_shooting == True, a função gera 
        um novo projétil do jogador de 50 em 50 frames, 
        junto com o som de disparo."""
        now = pygame.time.get_ticks()
        if self.auto_shooting and now - self.shoot_timer >= self.shoot_interval:
            self.shoot_timer = now
            bullet_sprites.add(self.create_bullet())
            shooting_sound.play()

    def bullet(self):
        """Gera um novo projétil se determinado intervalo
        de tempo for percorrido."""
        now = pygame.time.get_ticks()
        if now - self.shoot_timer >= self.shoot_interval_2:
            self.shoot_timer = now
            bullet_sprites.add(self.create_bullet())
            shooting_sound.play()

    def double_shot(self):
        """Gera dois projéteis seguidos e para."""
        now = pygame.time.get_ticks()
        if self.shooting and now - self.shoot_timer >= self.shoot_interval_3:
            self.shoot_timer = now
            bullet_sprites.add(self.create_bullet())
            shooting_sound.play()
            self.countt += 1
        if self.countt == 2:
            self.shooting = False
            self.countt = 0

    def score(self):
        # Quando a taxa de geração de inimigos aumenta, o self.score_add é multiplicado por 2.
        if self.score_count == 1200 and background.enemy_frequency != 200:
            self.score_add *= 2
            self.score_count = 0
        if collision_check(bullet_sprites, enemy_sprites):
            self.player_score += self.score_add
        elif collision_check(enemy_bullet_sprites, player_sprites):
            self.game_active = False


player = Player()
