from OpenGL.GL import *
from PIL import Image

def carregar_textura(caminho_img):
    img = Image.open(caminho_img) #abre a imagem usando a biblioteca pillow

    #converte os dados do pgn para o formato de leitura do opengl
    img = img.convert("RGBA")
    img_data = img.tobytes("raw", "RGBA") 
    
    textura_id = glGenTextures(1) #cria um endereço na memória para 1 textura criada
    
    glBindTexture(GL_TEXTURE_2D, textura_id) #binda o id à textura carregada
    
    # renderização da imagem 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)   # GL_TEXTURE_MIN_FILTER e GL_TEXTURE_MAG_FILTER dizem como a textura deve ser "esticada"
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)   # GL_LINEAR suaviza os pixels, evitando que a imagem pareça "quadriculada" quando esticada
    
    # envio de dados de pixel para a GPU
        # GL_RGBA - Formato dos dados da imagem (4 canais: R, G, B, A)
        # img.width, img.height - Dimensões da imagem
        # GL_UNSIGNED_BYTE - O tipo de dado de cada canal (número inteiro de 0 a 255)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    return textura_id, img.width, img.height

def desenhar_sprite(textura_id, x, y, width, height):
    glEnable(GL_TEXTURE_2D) # ativa a funcionalidade de sprites do opengl

    glBindTexture(GL_TEXTURE_2D, textura_id) # informa qual textura será usada 

    glBegin(GL_QUADS) # inicializa o objeto ortografico poligonal de 4 vértices (usando a função gl_quads, o opengl ja cria um quadrado com 2 triangulos, a base da computação gráfica)

    #SUP ESQUERDO   
    glTexCoord2f(0.0, 0.0) # escolhemos o canto superior esquerdo para inicializar as texturas do objeto criado
    glVertex2f(x + width, y) # coordenadas do canto da tela

    #SUP DIREITO
    glTexCoord2f(1.0, 0.0) # agora, criamos o canto superior direito 
    glVertex2f(x + width, y)

    #INF DIREITO
    glTexCoord2f(1.0, 1.0) # criamos o canto inferior direito
    glVertex2f(x + width, y + height) # e adicionamos a coordenada na tela

    #INF ESQUERDO
    glTexCoord2f(0.0, 1.0) # criamos o canto inferior esquerdo
    glVertex2f(x, y + height) # add as coordenadas

    glEnd() #finaliza o desenho do quadrado onde "colaremos as texturas"

    glDisable(GL_TEXTURE_2D) # e desativamos a funcionalidade de texturas para evitar desenhos desnecessários