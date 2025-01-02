import pygame
from constants import player_speed

pygame.init()

def update_player_pos(player_x_pos, player_y_pos):
  keys = pygame.key.get_pressed()

  if keys[pygame.K_w]:
    player_y_pos -= player_speed
  if keys[pygame.K_s]:
    player_y_pos += player_speed
  if keys[pygame.K_a]:
    player_x_pos -= player_speed
  if keys[pygame.K_d]:
    player_x_pos += player_speed
  
  return [player_x_pos, player_y_pos]