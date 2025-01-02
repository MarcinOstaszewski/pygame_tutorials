import pygame
from keys import update_player_pos

pygame.init()

spydey_surf = pygame.image.load('.\\graphics\\spydey.jpg').convert_alpha()
spydey_rect = spydey_surf.get_rect(topleft = (80, 80))
player_surf = pygame.image.load('.\\graphics\\archer.png').convert_alpha()

vac_01_surf = pygame.image.load('.\\graphics\\vac_01.svg')
vac_01_rect = vac_01_surf.get_rect(center = (300, 400))

def get_player(player_x_pos, player_y_pos):
  player_x_pos, player_y_pos = update_player_pos(player_x_pos, player_y_pos)
  player_rect = player_surf.get_rect(topleft = (player_x_pos, player_y_pos))
  return (player_surf, player_rect)
  