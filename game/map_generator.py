from sprite_renderer import *

TILE_SIZE = 16
ESCALA = 2

#UNWAKABLE_TILES = {24,25,26,27,28,29,56,61,184,185,186,187,188,189}

def carregar_mapa(caminho_mapa):
    mapa = []
    with open(caminho_mapa, 'r') as f:
        for linha in f.readlines():
            mapa.append([int(i) for i in linha.split()])
    return mapa

def render_mapa(mapa_dados, tileset_id, tileset_largura, tileset_altura):
    for y_tile, linha in enumerate(mapa_dados):
        for x_tile, tile_id in enumerate(linha):
            if tile_id != -1:
                tileset_colunas = tileset_largura // TILE_SIZE
                tex_x = (tile_id % tileset_colunas) * TILE_SIZE / tileset_largura
                tex_y = (tile_id // tileset_colunas) * TILE_SIZE / tileset_altura
                desenhar_sprite(
                    tileset_id,
                    x_tile * TILE_SIZE * ESCALA,
                    y_tile * TILE_SIZE * ESCALA,
                    TILE_SIZE * ESCALA,
                    TILE_SIZE * ESCALA,
                    tex_x, tex_y,
                    TILE_SIZE / tileset_largura,
                    TILE_SIZE / tileset_altura
                )