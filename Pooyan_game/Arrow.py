import pygame as pg
from Piggy_lift import Piggy_lift
from load_image import load_image
from constants import horizontal_center

class Arrow(pg.sprite.Sprite):
  """represents shooting projectile"""
  
  def __init__(self, piggy):
    pg.sprite.Sprite.__init__(self)
    self.image, self.rect = load_image("arrow_no_bg.png", -1, 1)
    screen = pg.display.get_surface()
    self.area = screen.get_rect()
    self.posX, self.posY, self.speedX, self.speedY = [0, 0, 0, 0]
    self.charge_x = 0.3
    self.speedY_change = 0.1
    self.speedX_friction = 0.997
    self.max_speed = 16
    self.piggy = piggy
    self.flying = False
    
  def update(self, keys):
    if self.flying:
      self._fly()
    else:
      if keys[pg.K_d]:
        height, self.speedY = Piggy_lift.get_height_and_speed(self.piggy)
        self.posX, self.posY = horizontal_center - 21, height + 26
        self.rect.center = (self.posX, self.posY)
        if self.speedX < self.max_speed:
          self.speedX += self.charge_x
      elif self.speedX > 0:
        self.flying = True

  def _fly(self):
    if self.posX > -self.rect.width/2 and self.rect.bottom < self.area.bottom + self.rect.height:
      self.posX, self.posY = (self.posX - 2*self.speedX, self.posY+self.speedY)
      self.rect.center = (self.posX, self.posY)
      self.speedY += self.speedY_change
      self.speedX *= self.speedX_friction
      if self.speedX < 0.1:
        self.speedX = 0

    else:
      self.speedX = 0
      self.speedY = 0
      self.flying = False
      