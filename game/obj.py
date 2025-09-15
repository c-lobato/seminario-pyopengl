import pygame as pg 

class Square():
    def __init__(self, col, x, y):
        self.image = pg.Surface((50,50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

square = Square("blue", 400,300)

print(square)