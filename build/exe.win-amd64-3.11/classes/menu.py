import pygame
from basic_game_config import screen_width, aliceblue, font


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.game_menu = True
        self.menu_txt = font.render(
            "The Mandalorian Guardian".upper(), True, aliceblue)
        self.menu_txt_rect = self.menu_txt.get_rect(
            center=(screen_width/2, 300))
        self.play = font.render("Play", True, aliceblue)
        self.play_rect = self.play.get_rect(center=(screen_width/2, 400))


menu = Menu()
