import pygame
pygame.init()

font_path = "fuente.ttf"
font = pygame.font.Font(font_path, 36)

MINIMO = 40
TAMANNO_LETRA = 30
TAMANNO_LETRA_GRANDE = 80
FPS_inicial = 3
TIEMPO_MAX = 61
N = 6

ANCHO = 800
ALTO = 600
COLOR_LETRAS = (20,200,20)
COLOR_FONDO =  ( 0, 128, 128)
COLOR_FONDO_MAL = (255, 0, 0)
COLOR_FONDO_BIEN = (0,128,0)
COLOR_TEXTO = (200,200,100)
COLOR_TIEMPO_FINAL = (200,20,10)
MARGEN = 1000
ESPACIO = 50

text = font.render("¿...Qué articulo tiene un precio parecido o igual que...?", True, (0, 0, 0))

text_rect = text.get_rect()
text_rect.center = (ANCHO // 2, ALTO // 10)




