import pygame as pg
from sprite_renderer import *
from map_generator import TILE_SIZE, ESCALA

class Character: 
    def __init__(self, x,y, width, height, velocidade, tile_size, escala):
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
        self.direcao = 'front'
        self.target_x = self.x
        self.target_y = self.y 
        self.frame_atual = 1
        self.frame_timer = 1
        self.frame_delay = 12

        self.sprites = {
            'idle_front': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\idle_front.png")[0],
            'idle_back': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\idle_back.png")[0],
            'idle_left': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\idle_left.png")[0],
            'idle_right': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\idle_right.png")[0],
            'walk_front_1': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_front_1.png")[0],
            'walk_front_2': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_front_2.png")[0],
            'walk_back_1': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_back_1.png")[0],
            'walk_back_2': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_back_2.png")[0],
            'walk_left_1': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_left_1.png")[0],
            'walk_left_2': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_left_2.png")[0],
            'walk_right_1': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_right_1.png")[0],
            'walk_right_2': carregar_textura(r"C:\Users\caiol\Documents\caio\FACULDADE\sistmult\seminario 1ee PARTE 2\seminario-pyopengl\game\assets_\sprites\ezgif-split\walk_right_2.png")[0],
        }

    def update_char(self, teclas):
        #bind das teclas
        if self.estado == self.IDLE:
            if teclas[pg.K_w]:
                self.target_y -= self.tile_size * self.escala
                self.direcao = 'back'
                self.estado = self.MOVING
            
            elif teclas[pg.K_s]:
                self.target_y += self.tile_size * self.escala
                self.direcao = 'front'
                self.estado = self.MOVING
          
            elif teclas[pg.K_a]:
                self.target_x -= self.tile_size * self.escala
                self.direcao = 'left'
                self.estado = self.MOVING
              
            elif teclas[pg.K_d]:
                self.target_x += self.tile_size * self.escala
                self.direcao = 'right'
                self.estado = self.MOVING

                
            #logica de chegada/destino (aumento/diminuição de velocidade)
        elif self.estado == self.MOVING:
            self.frame_timer += 1
            if self.frame_timer >= self.frame_delay:
                self.frame_atual = 1 if self.frame_atual == 2 else 2 # Alterna entre 1 e 2
                self.frame_timer = 0

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
        if self.estado == self.MOVING:
            sprite_key = f'walk_{self.direcao}_{self.frame_atual}'
        else:
            sprite_key = f'idle_{self.direcao}'
       
        sprite_id = self.sprites.get(sprite_key, self.sprites['idle_front'])
       
        #ajustando o posicionamento do sprite em relação ao mapa (offset)
        offset_y = (self.height - self.tile_size)
        ajuste_y = self.y + offset_y * escala

        func(sprite_id, self.x, ajuste_y, self.width * escala, self.height * escala, 0.0, 0.0, 1.0, 1.0)
                                                                                        #^^^^^^^^^^^^^^^^^^^^
                                                                                        #coordenadas da criação do quadrado