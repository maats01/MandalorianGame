import pygame

def collision_check(group1, group2):
    """Checagem de colisão entre qualquer elemento 
    de dois grupos de sprites."""
    return pygame.sprite.groupcollide(group1, group2, True, True, pygame.sprite.collide_mask)