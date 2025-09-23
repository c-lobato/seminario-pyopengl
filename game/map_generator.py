from sprite_renderer import *

TILE_SIZE = 16
ESCALA = 2

UNWAKABLE_TILES = {24,25,26,27,28,29,56,61,184,185,186,187,188,189}

def carregar_mapa(caminho_mapa):
    mapa = []
    with open(caminho_mapa, 'r') as f:
        for linha in f.readlines():
            mapa.append([int(i) for i in linha.split()])
    return mapa

def is_tile_walkable(x, y, mapa_dados):
    #converte a posição em pixel para a posição do tile no mapa
    x_mapa = int(x / (TILE_SIZE * ESCALA))
    y_mapa = int(y / (TILE_SIZE * ESCALA))

    #verifica se as coordenadas estão dentro dos limites do mapa
    if y_mapa < 0 or y_mapa >= len(mapa_dados) or x_mapa < 0 or x_mapa >= len(mapa_dados[0]):
        return False
        
    #pega o ID do tile de destino
    tile_id = int(mapa_dados[y_mapa][x_mapa])

    #retorna True se o tile não estiver no set de intransitáveis
    return tile_id not in UNWAKABLE_TILES 