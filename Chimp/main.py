from os import path
import pygame as pg
from load_sound import load_sound
from Chimp import Chimp
from Fist import Fist

pg.init()  # Initialize Pygame
screen = pg.display.set_mode((1280, 480), pg.SCALED)  # Set the display mode

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = path.split(path.abspath(__file__))[0]
sounds_dir = path.join(main_dir, "sounds")

whiff_sound = load_sound(sounds_dir, "whiff.mp3")
punch_sound = load_sound(sounds_dir, "punch.mp3")
chimp = Chimp(pg)
fist = Fist()
allsprites = pg.sprite.RenderPlain((chimp, fist))
clock = pg.time.Clock()

def main():
    pg.display.set_caption("Hit Chimp")
    pg.mouse.set_visible(False)
    
    bg = pg.Surface(screen.get_size()).convert()
    bg.fill((170, 238, 187))
    
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Smash the Chimp", True, (10, 10, 10))
        textpos = text.get_rect(centerx=bg.get_width() / 2, y=10)
        bg.blit(text, textpos)
        
    playing = True
    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                playing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pg.MOUSEBUTTONUP:
                fist.unpunch()

        clock.tick(60)
        allsprites.update()
        screen.blit(bg, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()
        
    pg.quit()
    exit()
    
if __name__ == "__main__":
    main()