import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from sprite_renderer import carregar_textura, desenhar_sprite

pg.init()

# configura as dimensões da janela e o título
screen_width, screen_height = 800, 600
pg.display.set_caption("Demonstração OpenGL")

# configura os atributos do OpenGL no Pygame
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 2)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 1)
pg.display.gl_set_attribute(pg.GL_DOUBLEBUFFER, 1)
pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

# cria a janela com suporte a OpenGL
screen = pg.display.set_mode((screen_width, screen_height), pg.OPENGL | pg.DOUBLEBUF)

# define a projeção ortográfica 
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_width, screen_height, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# habilita o blend para transparência
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# carrega a textura e pega as dimensões da imagem
# SUBSTITUA O CAMINHO ABAIXO PELO CAMINHO CORRETO DA SUA SPRITE SHEET
personagem_textura_id, sheet_width, sheet_height = carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\red\idle_front.png")

# define a posição inicial do personagem e as dimensões de exibição
personagem_x, personagem_y = 100, 100
velocidade_personagem= 2
relogio = pg.time.Clock()


# loop principal do jogo
running = True
while running:
    # gerenciamento de Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #logica do teclado
    teclas = pg.key.get_pressed()
    if teclas[pg.K_w]:
        personagem_y -= velocidade_personagem
    if teclas[pg.K_a]:
        personagem_x -= velocidade_personagem
    if teclas[pg.K_d]:
        personagem_x += velocidade_personagem
    if teclas[pg.K_s]:
        personagem_y += velocidade_personagem

    # renderização OpenGL
    glClear(GL_COLOR_BUFFER_BIT)
    
    # desenha o personagem
    desenhar_sprite(personagem_textura_id, personagem_x, personagem_y, largura_personagem, altura_personagem)
    # atualiza a tela
    pg.display.flip()

    relogio.tick(60) #limita os frames para 60 fps
    
# finaliza o Pygame
pg.quit()