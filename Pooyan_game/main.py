import pygame as pg
from Piggy_lift import Piggy_lift
from Arrow import Arrow

pg.init()
screen = pg.display.set_mode((1280, 720), pg.SCALED)

def main():
  pg.display.set_caption("Pooyan clone")
  bg = pg.Surface(screen.get_size()).convert()
  bg.fill((41, 38, 128))
  vertical_center = bg.get_height() / 2
  piggy = Piggy_lift()
  arrow = Arrow(piggy)
  allsprites = pg.sprite.RenderPlain((piggy, arrow))
  clock = pg.time.Clock()

  playing = True
  while playing:
    clock.tick(60)
    
    for event in pg.event.get():
      if event.type == pg.QUIT:
        playing = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          playing = False

    keys = pg.key.get_pressed()        
    allsprites.update(keys)
    
    screen.blit(bg, (0, 0))
    allsprites.draw(screen)
    pg.display.flip()
  
  
if __name__ == "__main__":
    main()