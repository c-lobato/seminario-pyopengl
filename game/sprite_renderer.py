from OpenGL.GL import *
from PIL import Image

def carregar_textura(caminho_imagem):
    """
    Carrega uma imagem e a converte em uma textura OpenGL.
    Retorna o ID da textura, largura e altura da imagem.
    """
    img = Image.open(caminho_imagem)
    img_data = img.convert("RGBA").tobytes()
    
    textura_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    return textura_id, img.width, img.height

def desenhar_sprite(textura_id, x, y, largura, altura, tex_x, tex_y, tex_largura, tex_altura):

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)     #cria o quadrado onde "colaremos" todas as texturas por cima
    
    #canto superior esquerdo da figura 
    glTexCoord2f(tex_x, tex_y)
    glVertex2f(x, y)
    
    #canto superior direito 
    glTexCoord2f(tex_x + tex_largura, tex_y)
    glVertex2f(x + largura, y)
    
    #canto inferior direito
    glTexCoord2f(tex_x + tex_largura, tex_y + tex_altura)
    glVertex2f(x + largura, y + altura)
    
    #canto inferior esquerdo
    glTexCoord2f(tex_x, tex_y + tex_altura)
    glVertex2f(x, y + altura)

    glEnd()
    glDisable(GL_TEXTURE_2D)