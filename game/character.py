import pygame as pg
from sprite_renderer import *

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
    
    #movimentação do personagem + atualização de posicionamento no tileset
    def update_char(self, teclas, mapatras, unwalkable_tiles):
        if self.estado == self.IDLE:
            if teclas[pg.K_w]:
                self.target_y -= self.tile_size * self.escala
                self.estado = self.MOVING
            elif teclas[pg.K_s]:
                self.target_y += self.tile_size * self.escala
                self.estado = self.MOVING
            elif teclas[pg.K_a]:
                self.target_x -= self.tile_size * self.escala
                self.estado = self.MOVING
            elif teclas[pg.K_d]:
                self.target_x += self.tile_size * self.escala
                self.estado = self.MOVING
            
        #logica de chegada/destino (aumento/diminuição de velocidade)
        elif self.estado == self.MOVING:
            if self.x < self.target_x:
                self.x += self.velocidade
            if self.x > self.target_x:
                self.x -= self.velocidade
            if self.y < self.target_y:
                self.y += self.velocidade
            if self.y > self.target_y:
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


