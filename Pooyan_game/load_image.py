from os import path
import pygame as pg

def load_image(name, colorkey=None, scale=1):
  main_dir = path.split(path.abspath(__file__))[0]
  images_dir = path.join(main_dir, "data")
  fullname = path.join(images_dir, name)
  image = pg.image.load(fullname)
  
  size = image.get_size()
  size = (size[0] * scale, size[1] * scale)
  image = pg.transform.scale(image, size)
  
  image = image.convert()

  if colorkey is not None:
    if colorkey == -1:
      colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey, pg.RLEACCEL)
  return image, image.get_rect()