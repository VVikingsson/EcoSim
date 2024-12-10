import pygame as pg
from settings import *
from Environment import Environment
from HeadsUpDisplay import HeadsUpDisplay

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pg.Clock()
    running = True
    environment = Environment()
    hud = HeadsUpDisplay()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(hud, (0,0))
        pg.display.flip()
        
        
        clock.tick(60)



if __name__ == "__main__":
    main()