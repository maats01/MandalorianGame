import pygame

# fps 
clock = pygame.time.Clock()
fps = 60

# tamanho da janela
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Mandalorian Guardian")

# cores
aliceblue = pygame.Color("aliceblue")
black = pygame.Color("black")

# fonte
pygame.font.init()
font = pygame.font.Font("Fonte/Orbitron-Regular.ttf", 32)
