import pygame
from basic_game_config import screen_height


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, type, pos_x, pos_y):
        super().__init__()
        if type == "enemy_1.png":
            self.image = pygame.image.load(
                'Sprites/enemies/laser.png').convert_alpha()
            self.bullet_speed = 10
        else:
            self.image = pygame.image.load(
                'Sprites/enemies/laser_2.png').convert_alpha()
            self.bullet_speed = 8
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        """A cada frame do jogo, incrementa o valor da variável
        self.bullet_speed no eixo y do projétil dos inimigos. 
        Se o projétil estiver abaixo da borda da tela, ele é deletado."""
        self.rect.y += self.bullet_speed
        if self.rect.top >= screen_height:
            self.kill()
