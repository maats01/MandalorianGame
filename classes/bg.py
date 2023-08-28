import pygame
from math import ceil
from random import randint, choice
from basic_game_config import screen_height, screen_width, screen
from classes.enemy import Enemy
from classes.menu import menu
from sprite_groups import enemy_sprites


class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'Sprites/background/bg.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (screen_width, screen_height))
        self.rect = self.image.get_rect()
        self.scroll = 0
        self.bg_height = self.image.get_height()
        self.tiles = ceil(screen_height/self.bg_height)+1
        self.count = 0
        self.enemy_timer = pygame.time.get_ticks()
        self.enemy_timer_2 = self.enemy_timer
        self.enemy_frequency = 1600  # ms

    def update(self):
        """Coloca na tela duas imagens, uma em cima da outra.
        A cada frame do jogo, essa função vai incrementar o y
        de ambas as imagens, fazendo elas descerem."""
        self.count += 1
        for i in range(0, self.tiles):
            self.rect.y = i*self.bg_height*(-1)+self.scroll
            screen.blit(self.image, self.rect)

        self.scroll += 6
        if self.scroll > self.bg_height:
            self.scroll = 0

    def create_enemy(self):
        """Aumenta a taxa de geração de inimigos conforme
        o tempo vai passando e gera inimigos aleatórios 
        em posições aleatórias do lado de fora da tela."""
        if self.count >= 1200 and self.enemy_frequency != 200:
            self.enemy_frequency -= 200
            self.count = 0

        now = pygame.time.get_ticks()
        if now - self.enemy_timer >= self.enemy_frequency:
            self.enemy_timer = now
            # escolhe um tipo de inimigo
            enemy_type = choice(["enemy_1.png", "enemy_2.png"])

            # carrega a imagem do inimigo escolhido
            enemy_image = pygame.image.load(
                f"Sprites/enemies/{enemy_type}").convert_alpha()

            # define valores aleatórios para o eixo x (fora da tela) e y do inimigo
            enemy_pos_x = randint(-750, -enemy_image.get_width())
            enemy_pos_y = randint(0, enemy_image.get_height() + 150)

            # criando um retângulo com a altura um pouco maior para o inimigo
            enemy_rect = pygame.Rect(
                enemy_pos_x, enemy_pos_y-200, enemy_image.get_width(), 500)

            for enemy in enemy_sprites:
                """checando se há colisão entre o inimigo gerado com os que já
                foram gerados, se há colisão, o novo inimigo não é gerado."""
                if enemy_rect.colliderect(enemy.rect):
                    return

            # gerando o inimigo e adicionando no grupo de inimigos
            enemy = Enemy(enemy_image, enemy_type, enemy_pos_x, enemy_pos_y)
            enemy_sprites.add(enemy)
