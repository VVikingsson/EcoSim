import pygame as pg
from settings import *
from Environment import Environment
def repaint(environemnt):


def main():
    pg.init()
    screen = pg.display.set_mode((HEIGHT, WIDTH))

    clock = pg.Clock()
    running = True
    environment = Environment()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        repaint(environment)
        clock.tick(60)



if __name__ == "__main__":
    main()