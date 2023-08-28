from basic_game_config import screen_width, screen_height
from classes.timerClass import timer
from classes.player import player, background
from sprite_groups import enemy_bullet_sprites, enemy_sprites, bullet_sprites, player_sprites


def restart():
    """Restart vai redefinir valores de variáveis
    importantes para o jogo recomeçar do zero."""
    player.game_active = True
    player.game_time = timer.set(0)
    player.player_score = 0
    player.rect.center = screen_width/2, screen_height - 80
    player.auto_shooting = False
    player.count = 1
    player.score_add = 5
    player.score_count = 0

    background.count = 0
    background.enemy_frequency = 1600

    player_sprites.add(player)

    # excluindo todos os sprites dos grupos abaixo
    enemy_sprites.empty()
    bullet_sprites.empty()
    enemy_bullet_sprites.empty()
