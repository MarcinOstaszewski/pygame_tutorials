import pygame
from sprites import player_rect, spydey_rect

pygame.init()
mouse_pos = pygame.mouse.get_pos()

if player_rect.colliderect(spydey_rect):
  print(1)
    
if player_rect.collidepoint(mouse_pos):
  print('mouse inside of the player')
else:
  print('not inside')