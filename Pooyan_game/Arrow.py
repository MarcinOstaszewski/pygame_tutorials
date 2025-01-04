import pygame as pg
from load_image import load_image

class Arrow(pg.sprite.Sprite):
  """represents shooting projectiles"""
  
  def __init__(self, charged_arrow_rect, charge_value, speedY):
    pg.sprite.Sprite.__init__(self)
    self.image, self.rect = load_image("arrow_no_bg.png", -1, 1)
    screen = pg.display.get_surface()
    self.area = screen.get_rect()
    self.rect = charged_arrow_rect.move(0, speedY)
    self.speedX = charge_value
    self.speedY = speedY
    self.speedY_change = 0.1
    self.speedX_friction = 0.997
    self.max_speed = 16
    
  def update(self, _):
    if self.rect.right > 0 and self.rect.top < self.area.bottom:
      self.rect.move_ip(-2 * self.speedX, self.speedY)
      self.speedY += self.speedY_change
      self.speedX *= self.speedX_friction
      if self.speedX < 0.1:
        self.speedX = 0
    else:
      self.kill()