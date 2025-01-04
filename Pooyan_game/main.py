import pygame as pg
from Piggy_lift import Piggy_lift
from exit_events import check_for_exit_events
from sprite_utils import add_to_allsprites

pg.init()
screen = pg.display.set_mode((1280, 720), pg.SCALED)
allsprites = pg.sprite.RenderPlain()

def main():
  pg.display.set_caption("Pooyan clone")
  bg = pg.Surface(screen.get_size()).convert()
  bg.fill((41, 38, 128))
  piggy = Piggy_lift(allsprites, add_to_allsprites)
  add_to_allsprites(allsprites, piggy)
  clock = pg.time.Clock()

  playing = True
  while playing:
    clock.tick(60)
    playing = check_for_exit_events(pg)

    # update sprites with keyboard events
    keys = pg.key.get_pressed()
    allsprites.update(keys)
    
    # update screen and sprites
    screen.blit(bg, (0, 0))
    allsprites.draw(screen)
    pg.display.flip()
  
  
if __name__ == "__main__":
  main()