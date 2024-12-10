import pygame as pg
from settings import *

class HeadsUpDisplay(pg.Surface):
    def __init__(self):
        super().__init__((SCREEN_WIDTH, HUD_HEIGHT))

        self.initialize_fonts()
        self.initialize_panels()
        self.temp_image = pg.image.load("assets/EcoSim_HUD_sketch.png")
        self.temp_image = pg.transform.scale_by(self.temp_image, 2)
        self.redraw_contents()

    def initialize_fonts(self):
        self.font = pg.freetype.Font("fonts/ByteBounce.ttf", size=20)
    
    def initialize_panels(self):
        self.timer = self.font.render("TIMER TEXT GOES HERE", True, pg.Color(0,0,0))[0]
        

    def redraw_contents(self):
        self.blit(self.temp_image, (0,0))
        self.blit(self.timer, (20,20))
