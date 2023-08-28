import pygame
from math import trunc
from functions.collision import collision_check
from functions.restart import restart
from classes.timerClass import timer
from classes.player import player, background
from classes.menu import menu
from sounds import *
from basic_game_config import *
from sprite_groups import *


pygame.init()


player_sprites.add(player)
bg_sprite.add(background)

# looping principal do jogo
while True:
    # fps do jogo
    clock.tick(fps)

    # pega os inputs do teclado do player
    keys = pygame.key.get_pressed()

    # fechar janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if menu.game_menu:
            # comandos dentro do menu do jogo
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.play_rect.collidepoint(pygame.mouse.get_pos()):
                    player.game_time = timer.set(0)
                    background.playing = True
                    menu.game_menu = False
                    player.game_active = True
                                                                                                        
        if player.game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j: # disparo manual
                    player.bullet()
                if event.key == pygame.K_l: # disparo duplo
                    player.shooting = True
                    
                # mecânica de disparo automático
                if event.key == pygame.K_k and player.count < 2:
                    player.auto_shooting = True
                    player.count += 1
                elif event.key == pygame.K_k and player.count == 2:
                    player.auto_shooting = False
                    player.count = 1

        elif not (player.game_active) and not (menu.game_menu):
            # comandos da tela de morte
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    if player.game_active:
        player.game_time = timer.get()
        # lógica de disparo do player
        player.auto_bullet()
        player.double_shot()

        # lógica dos projéteis dos inimigos
        for enemy in enemy_sprites:
            # basicamente o inimigo 1 atira mais rápido que o inimigo 2
            if enemy.enemy_type == "enemy_1.png":
                enemy.bullet_rate = 30
            else:
                enemy.bullet_rate = 60

            if enemy.count >= enemy.bullet_rate and enemy.rect.right > 0:
                enemy.count = 0
                enemy_bullet_sprites.add(enemy.create_bullet())
                shooting_sound.play()

        # lógica do score do player
        player.score()

        # checa colisão entre projéteis
        bullets_to_bullets = collision_check(
            bullet_sprites, enemy_bullet_sprites)

        # movimento do player
        player.player_inputs(keys)

        # desenhando os sprites
        bg_sprite.update()
        background.create_enemy()
        bullet_sprites.draw(screen)
        enemy_bullet_sprites.draw(screen)
        player_sprites.draw(screen)
        enemy_sprites.draw(screen)

        # cronometro
        tempo_txt = font.render(
            f"Tempo: {trunc(player.game_time)}", True, aliceblue)
        screen.blit(tempo_txt, (10, 10))

        # score
        score_txt = font.render(
            f"Score: {player.player_score}", True, aliceblue)
        screen.blit(score_txt, (screen_width - 10 - score_txt.get_width(), 10))

        # atualização dos sprites
        player_sprites.update()
        bullet_sprites.update()
        enemy_bullet_sprites.update()
        enemy_sprites.update()

        if not pygame.mixer.music.get_busy():   # lógica para tocar a música de fundo
            pygame.mixer.music.play(loops=-1)

    else:
        screen.fill(black)
        if menu.game_menu:  # textos do menu do jogo
            screen.blit(menu.menu_txt, menu.menu_txt_rect)
            screen.blit(menu.play, menu.play_rect)

        else:   # tela de morte
            pygame.mixer.music.stop()

            gameover_txt1 = font.render(
                f"Tempo: {trunc(player.game_time)}s   Score: {player.player_score}", True, aliceblue)
            gameover_txt2 = font.render(
                f"Pressione 'Espaço' para recomeçar ou 'Esc' para sair", True, aliceblue)

            screen.blit(gameover_txt1, gameover_txt1.get_rect(
                center=(screen_width/2, screen_height/2)))
            screen.blit(gameover_txt2, gameover_txt2.get_rect(
                center=(screen_width/2, screen_height/2+50)))

    pygame.display.flip()
