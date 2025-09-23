from sprite_renderer import *

UNWAKABLE_TILES = {24,25,26,27,28,29,56,39,184,185,186,187,188,189}

def carregar_mapa(caminho_mapa):
    mapa = []
    with open(caminho_mapa, 'r') as f:
        for linha in f.readlines():
            mapa.append([int(i) for i in linha.split()])
    return mapa

