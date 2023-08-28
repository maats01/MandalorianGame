import pygame
from classes.enemy_bullet import EnemyBullet
from basic_game_config import screen_width


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, enemy_type, pos_x, pos_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.enemy_type = enemy_type
        self.enemy_speed = 5
        self.count = 0

    def update(self):
        """A cada frame do jogo, incrementa o valor da variável
        self.enemy_speed no eixo x do inimigo. Se o inimigo
        estiver fora da borda direita da tela, ele é deletado."""
        self.count += 1
        self.rect.x += self.enemy_speed
        if self.rect.x > screen_width:
            self.kill()

    def create_bullet(self):
        return EnemyBullet(self.enemy_type, self.rect.midbottom[0], self.rect.midbottom[1])
