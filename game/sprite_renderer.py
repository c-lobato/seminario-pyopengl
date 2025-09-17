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

def desenhar_sprite(textura_id, x, y, largura, altura):
    """
    Desenha um sprite na tela nas coordenadas especificadas.
    """
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    
    # As coordenadas de textura agora cobrem a imagem inteira
    glTexCoord2f(0.0, 0.0)
    glVertex2f(x, y)
    
    glTexCoord2f(1.0, 0.0)
    glVertex2f(x + largura, y)
    
    glTexCoord2f(1.0, 1.0)
    glVertex2f(x + largura, y + altura)
    
    glTexCoord2f(0.0, 1.0)
    glVertex2f(x, y + altura)

    glEnd()
    glDisable(GL_TEXTURE_2D)