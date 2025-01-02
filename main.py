
import pygame
from sys import exit
from screen_conf import get_updated_screen 
from sprites import get_player#, spydey_surf, spydey_rect
from constants import screen_width , screen_height
from keys import update_player_pos

def main():
  player_x_pos = screen_width / 2
  player_y_pos = screen_height / 2
  pygame.init()
  clock = pygame.time.Clock()
  start_game_time = 0
  is_playing = True
  
  vac_01_surf = pygame.image.load('.\\graphics\\vac_01.svg')
  vac_01_rect = vac_01_surf.get_rect(center = (300, 400))
  
  while is_playing:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      # if event.type == pygame.MOUSEMOTION:
      #   print(event.pos)
      if event.type == pygame.MOUSEBUTTONDOWN:
        start_game_time = pygame.time.get_ticks()
    
    player_x_pos, player_y_pos = update_player_pos(player_x_pos, player_y_pos)
    player_surf, player_rect = get_player(player_x_pos, player_y_pos)
    screen = get_updated_screen(int((current_time - start_game_time) / 100))
    # screen.blit(spydey_surf, spydey_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(vac_01_surf, vac_01_rect)
    
    pygame.display.update()
    clock.tick(60)
        

if __name__ == "__main__":
  main()