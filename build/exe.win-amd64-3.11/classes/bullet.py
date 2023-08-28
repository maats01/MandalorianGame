import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(
            'Sprites/player/laser.png').convert_alpha()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.bullet_speed = 12

    def update(self):
        """A cada frame é subtraído o valor da variável self.bullet_speed
        no eixo y do retângulo do projétil.Se o projétil estiver acima da 
        borda da tela, ele é deletado."""
        self.rect.y -= self.bullet_speed
        if self.rect.bottom <= 0:
            self.kill()
