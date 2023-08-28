import pygame

pygame.mixer.init()
# som de tiro
shooting_sound = pygame.mixer.Sound("Sons/shooting_sound.mp3")
shooting_sound.set_volume(0.7)

# música
pygame.mixer.music.load("Sons/Milenivm - Hacked.mp3")
pygame.mixer.music.set_volume(0.03)
