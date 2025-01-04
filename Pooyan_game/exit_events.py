def check_for_exit_events(pg):
  for event in pg.event.get():
    if event.type == pg.QUIT:
      return False
    elif event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE:
        return False

  return True