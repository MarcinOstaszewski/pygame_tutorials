import pygame
from constants import screen_width, screen_height

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Tutorial')

bg_surface = pygame.image.load('.\\graphics\\background_03.jpg').convert()
font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 35)
game_text_surf = font.render('My First Game', True, 'Red')
game_text_rect = game_text_surf.get_rect(center = (400, 50))

def update_score(start_game_time):
  score_surf = score_font.render(f'current score: {start_game_time}', True, "Black")
  score_rect = score_surf.get_rect(topleft = (0, 0))
  pygame.draw.rect(screen, 'Orange', score_rect, 15)
  pygame.draw.rect(screen, 'Orange', score_rect)
  screen.blit(score_surf, score_rect)

def get_updated_screen(start_game_time):
  screen.fill((0, 0, 0))
  screen.blit(bg_surface, (0, 0))
  update_score(start_game_time)
  screen.blit(game_text_surf, game_text_rect)
  return screen

