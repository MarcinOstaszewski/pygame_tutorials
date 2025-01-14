import pygame as pg
from load_image import load_image

class Balloon(pg.sprite.Sprite):
    """Represents a balloon that moves up the screen"""

    def __init__(self, color, position_x, start_time):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(f"baloon_{color}.png", -1, 1)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.midtop = (position_x, self.area.bottom + 10)  # Start below the screen
        self.speedY = -2
        self.start_time = start_time
        self.spawned = False

    def update(self, current_time):
        if current_time >= self.start_time:
            self.spawned = True
        if self.spawned:
            self.rect.move_ip(0, self.speedY)
            if self.rect.bottom < 0:
                self.kill()
