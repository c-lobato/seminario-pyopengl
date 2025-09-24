import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from sprite_renderer import * 
from character import Character
from map_generator import *

#inicialização do pygame
pg.init()

#cria o contador de frames do jogo
relogio = pg.time.Clock()

# configura as dimensões da janela e o título
screen_width, screen_height = 600, 600
pg.display.set_caption("pokemon paraguaio com opengl")

# configura os atributos do OpenGL no Pygame
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 2)  
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 1) #ativa a versão 2.1 do opengl
pg.display.gl_set_attribute(pg.GL_DOUBLEBUFFER, 1)  #ativa o double buffer do opengl
pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)  #"profundidade" do z-buffer 

# cria a janela com suporte a OpenGL
screen = pg.display.set_mode((screen_width, screen_height), pg.OPENGL | pg.DOUBLEBUF)

# define a projeção ortográfica 
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_width, screen_height, 0, -1, 1) #cria a matriz ortogonal
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# habilita o blend para transparência
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#carregamento do mapa e seus dados
tileset_id, tileset_largura, tileset_altura = carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\maps\simple_tileset_32x32_version1.0\tilesheet_basic.png") 
mapa_dados = carregar_mapa(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\maps\mapatras.txt")

#instanciação do personagem 
char = Character(x=1, y=1,width=16,height=24,velocidade=2, tile_size=TILE_SIZE, escala=ESCALA)

# loop principal do jogo
running = True
while running:
    # gerenciamento de Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #logica do teclado/movimentação
    teclas = pg.key.get_pressed()
    char.update_char(teclas) #chamada da atualização da posição do char

    # renderização OpenGL
    glClear(GL_COLOR_BUFFER_BIT)

    #renderização e desenho do mapa
    render_mapa(mapa_dados, tileset_id, tileset_largura, tileset_altura)
        
    # desenha o personagem
    char.draw_char(desenhar_sprite, ESCALA)

    # atualiza a tela
    pg.display.flip()

    #tickrate do game
    relogio.tick(60)    #limita os frames para 60 fps
    
# inicializa o Pygame
pg.quit() 