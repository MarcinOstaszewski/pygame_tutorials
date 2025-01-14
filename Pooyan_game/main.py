import pygame as pg
from Piggy_lift import Piggy_lift
from exit_events import check_for_exit_events
from sprite_utils import add_to_allsprites
from sprite_utils import add_to_allsprites, create_balloons
from balloon_sequence import balloon_sequence

pg.init()
screen = pg.display.set_mode((1280, 720), pg.SCALED)
allsprites = pg.sprite.RenderPlain()
balloons_group = pg.sprite.Group()

create_balloons(balloons_group, balloon_sequence)

def check_collisions(arrows_group, balloons_group):
  for arrow in arrows_group:
    # arrow_tip_rect = pg.Rect(arrow.rect.left, arrow.rect.top, arrow.rect.left + 5, arrow.rect.bottom - 10)
    for balloon in balloons_group:
      if balloon.rect.colliderect(arrow.rect): # arrow_tip_rect):
        print(f"arrow: {arrow.rect} hit balloon: {balloon.rect}") # .left, balloon.rect.top, balloon.rect.right, balloon.rect.bottom - 10}")
        balloon.kill()

def main():
  pg.display.set_caption("Pooyan clone")
  bg = pg.Surface(screen.get_size()).convert()
  bg.fill((41, 38, 128))
  arrows_group = pg.sprite.Group()
  piggy = Piggy_lift(allsprites, add_to_allsprites, arrows_group)
  add_to_allsprites(allsprites, piggy)
  clock = pg.time.Clock()
  start_ticks = pg.time.get_ticks()

  playing = True
  while playing:
    clock.tick(60)
    playing = check_for_exit_events(pg)

    # update sprites with keyboard events
    keys = pg.key.get_pressed()
    allsprites.update(keys)
    current_time = (pg.time.get_ticks() - start_ticks) / 1000
    balloons_group.update(current_time)
    arrows_group.update(current_time)

    check_collisions(arrows_group, balloons_group)
    
    # update screen and sprites
    screen.blit(bg, (0, 0))
    allsprites.draw(screen)
    balloons_group.draw(screen)
    arrows_group.draw(screen)
    pg.display.flip()
  
  
if __name__ == "__main__":
  main()