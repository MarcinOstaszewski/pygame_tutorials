import pygame as pg
from Arrow import Arrow
from load_image import load_image
from constants import horizontal_center
from helpers.update_rect_position import update_rect_position

class Piggy_lift(pg.sprite.Sprite):
  """moves a lift up and down"""
    
  def __init__(self, allsprites, add_to_allsprites):
    pg.sprite.Sprite.__init__(self)
    screen = pg.display.get_surface()
    vertical_center = screen.get_height() / 2
    self.image, self.rect = load_image("piggy_lift_no_bg.png", -1, 1)
    self.area = screen.get_rect()
    self.rect.center = horizontal_center, vertical_center
    self.speedY = 0 
    self.speed_change = .15
    self.max_speed = 8
    self.allsprites = allsprites
    self.add_to_allsprites = add_to_allsprites

    # charge variables
    self.charge_value = 0
    self.charge_increase = 0.3
    self.max_charge = 16
    self.charged_arrow_rect = None
    
  @staticmethod
  def get_height_and_speed(piggy):
    return piggy.rect.center[1], piggy.speed
    
  def update(self, keys):
    if keys[pg.K_d]:
      self.charged_arrow_rect = self.rect.move(2, 80)
      if self.charge_value < self.max_charge:
        self.charge_value += self.charge_increase
        # add display charge bar (use some func from main.py)
    elif self.charge_value > 0:
      arrow_instance = Arrow(self.charged_arrow_rect, self.charge_value, self.speedY)
      self.add_to_allsprites(self.allsprites, arrow_instance)
      self.charge_value = 0
      
    if keys[pg.K_w]:
      if self.speedY > -self.max_speed:
        self.speedY -= self.speed_change
    elif keys[pg.K_s]:
      if self.speedY < self.max_speed:
        self.speedY += self.speed_change
    elif abs(self.speedY) < self.speed_change:
      self.speedY = 0
    else:
      self.speedY *= .97
      
    if self.speedY != 0:
      self = update_rect_position(self)