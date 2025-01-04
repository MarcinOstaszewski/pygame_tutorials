def update_rect_position(self):
  """Updates rect position."""

  distance = 30
  moved_rect = self.rect.move((0, self.speedY))
  if moved_rect.top >= distance and moved_rect.bottom <= self.area.bottom - distance:
    self.rect = moved_rect
  else:
    self.speedY = -self.speedY * 0.4
    self.rect = self.rect.move((0, self.speedY))

  return self
