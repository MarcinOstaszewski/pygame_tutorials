import pygame as pg
from load_image import load_image
from constants import horizontal_center

class Piggy_lift(pg.sprite.Sprite):
  """moves a lift up and down"""
    
  def __init__(self):
    pg.sprite.Sprite.__init__(self)
    screen = pg.display.get_surface()
    vertical_center = screen.get_height() / 2
    self.image, self.rect = load_image("piggy_lift_no_bg.png", -1, 1)
    self.area = screen.get_rect()
    self.rect.center = horizontal_center, vertical_center
    self.speed = 0
    self.speed_change = .15
    self.max_speed = 8
    
  @staticmethod
  def get_height_and_speed(piggy):
    return piggy.rect.center[1], piggy.speed

    
  def update(self, keys):
    if keys[pg.K_w]:
      if self.speed > -self.max_speed:
        self.speed -= self.speed_change
    elif keys[pg.K_s]:
      if self.speed < self.max_speed:
        self.speed += self.speed_change
    elif abs(self.speed) < self.speed_change:
      self.speed = 0
    else:
      self.speed *= .97
      
    if self.speed != 0:
      newpos = self.rect.move((0, self.speed))
      if not self.area.contains(newpos):
        if self.rect.bottom < (self.area.bottom) or self.rect.top > (self.area.top):
          newpos = self.rect.move((0, 0))
      self.rect = newpos