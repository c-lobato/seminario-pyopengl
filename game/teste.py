import pygame as pg
from pygame.locals import *
from OpenGL.GL import *

pg.init()
screen_width, screen_height = 800, 600
pg.display.set_caption("Teste OpenGL")
screen = pg.display.set_mode((screen_width, screen_height), pg.OPENGL | pg.DOUBLEBUF)

# Limpa a tela com uma cor de fundo escura
glClearColor(0.1, 0.1, 0.1, 1.0)
glClear(GL_COLOR_BUFFER_BIT)

# Configura a projeção ortográfica 2D
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_width, screen_height, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Loop principal
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Limpa a tela
    glClear(GL_COLOR_BUFFER_BIT)

    # Desenha um quadrado branco no centro da tela
    glColor3f(1.0, 1.0, 1.0) # Cor branca (RGB)
    glBegin(GL_QUADS)
    glVertex2f(350, 250)
    glVertex2f(450, 250)
    glVertex2f(450, 350)
    glVertex2f(350, 350)
    glEnd()

    # Atualiza a tela
    pg.display.flip()
    
pg.quit()