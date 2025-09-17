import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from sprite_renderer import carregar_textura, desenhar_sprite

#variáveis de renderização
TILE_SIZE = 16
ESCALA = 2

#função que inicializa o tileset do mapa
def carregar_mapa(caminho_mapa):
    mapa = []
    with open(caminho_mapa, 'r') as f:
        for linha in f.readlines():
            mapa.append([int(i) for i in linha.split()])
    return mapa

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

# loading das texturas do personagem e do mapa
personagem_textura_id, largura_personagem, altura_personagem = carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\red\idle_front.png")

tileset_id, tileset_largura, tileset_altura = carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\maps\mapa_generico.png")
mapa_data = carregar_mapa(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\maps\mapa.txt")

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

    #renderização e desenho do mapa
    for y_tile, linha in enumerate(mapa_data):
        for x_tile, tile_id in enumerate(linha):
            # calcula as coordenadas do tile no tileset
            tileset_colunas = tileset_largura // TILE_SIZE
            tex_x = (tile_id % tileset_colunas) * TILE_SIZE / tileset_largura
            tex_y = (tile_id // tileset_colunas) * TILE_SIZE / tileset_altura

            # desenha o tile
            desenhar_sprite(tileset_id, 
                            x_tile * TILE_SIZE * ESCALA, 
                            y_tile * TILE_SIZE * ESCALA, 
                            TILE_SIZE * ESCALA, TILE_SIZE * ESCALA,
                            tex_x, tex_y,
                            TILE_SIZE / tileset_largura, TILE_SIZE / tileset_altura)
        
    # desenha o personagem
    desenhar_sprite(personagem_textura_id, personagem_x, personagem_y, largura_personagem * ESCALA, altura_personagem * ESCALA, 0.0, 0.0, 1.0, 1.0)
    # atualiza a tela
    pg.display.flip()

    relogio.tick(60) #limita os frames para 60 fps
    
# inicializa o Pygame
pg.quit()