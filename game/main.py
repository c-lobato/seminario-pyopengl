import pygame as pg
from pygame.locals import * 

from OpenGL.GL import *

pg.init()
screen_width, screen_height = 700,600

#inicializa o opengl como motor grafico do pygame
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 2)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 1)
pg.display.gl_set_attribute(pg.GL_DOUBLEBUFFER, 1)
pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

#cria a janela com suporte ao opengl
screen = pg.display.set_mode((screen_width, screen_height), pg.OPENGL | pg.DOUBLEBUF)

glClearColor(0.0, 0.0, 0.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT)

#cria a projeção ortogonal (transforma a matriz 3d em 2d)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_width, screen_height, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

#loop de jogo
running = True
while running:
    #gerenciamento de eventos (Teclado, Mouse, etc.)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    pg.display.flip()

pg.quit()
