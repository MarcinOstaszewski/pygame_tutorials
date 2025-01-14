import pygame as pg
from Balloon import Balloon

def add_to_allsprites(allsprites, sprite):
  allsprites.add(sprite)

def create_balloons(balloons_group, sequence):
  for balloon_info in sequence:
    balloon = Balloon(balloon_info['color'], balloon_info['position_x'], balloon_info['time'])
    balloons_group.add(balloon)