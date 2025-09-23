import pygame as pg
from sprite_renderer import *
from map_generator import TILE_SIZE, ESCALA, is_tile_walkable

class Character: 
    def __init__(self, sprite_id, x,y, width, height, velocidade, tile_size, escala):
        self.sprite_id = sprite_id
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.velocidade = velocidade 
        self.tile_size = tile_size
        self.escala = escala

        self.IDLE = 0
        self.MOVING = 1
        self.estado = self.IDLE
        self.target_x = self.x
        self.target_y = self.y 
    
    def _try_move(self, new_x, new_y, mapa_dados):
        if self.estado == self.IDLE and is_tile_walkable(new_x, new_y, mapa_dados):
            self.target_x = new_x
            self.target_y = new_y
            self.estado = self.MOVING

    def update_char(self, teclas, mapa_dados):
        # lógica de movimento 
        if teclas[pg.K_w]:
            self._try_move(self.x, self.y - self.tile_size * self.escala, mapa_dados)
        elif teclas[pg.K_s]:
            self._try_move(self.x, self.y + self.tile_size * self.escala, mapa_dados)
        elif teclas[pg.K_a]:
            self._try_move(self.x - self.tile_size * self.escala, self.y, mapa_dados)
        elif teclas[pg.K_d]:
            self._try_move(self.x + self.tile_size * self.escala, self.y, mapa_dados)

        #logica de chegada/destino (aumento/diminuição de velocidade)
        elif self.estado == self.MOVING:
            if self.x < self.target_x:
                self.x += self.velocidade
            elif self.x > self.target_x:
                self.x -= self.velocidade
            elif self.y < self.target_y:
                self.y += self.velocidade
            elif self.y > self.target_y:
                self.y -= self.velocidade       

        #verificação de destino  
        if(abs(self.x - self.target_x) < self.velocidade) and (abs(self.y - self.target_y) < self.velocidade):
            self.x = self.target_x
            self.y = self.target_y
            self.estado = self.IDLE 
        
    #desenho do sprite do personagem 
    def draw_char(self, func, escala):
        #ajustando o posicionamento do sprite em relação ao mapa (offset)
        offset_y = (self.height - self.tile_size)
        ajuste_y = self.y + offset_y * escala

        func(self.sprite_id, self.x, ajuste_y, self.width * escala, self.height * escala, 0.0, 0.0, 1.0, 1.0)
                                                                                        #^^^^^^^^^^^^^^^^^^^^
                                                                                        #coordenadas da criação do quadrado