WIDTH = 600
VELKOST_POLA = 4
VELKOST_KARTY = WIDTH // VELKOST_POLA
HEIGHT = (VELKOST_POLA * VELKOST_KARTY) + 100
# Farby
BIELA = (255, 255, 255)
CIERNA = (0, 0, 0)
SIVA = (200, 200, 200)
MODRA = (0, 0, 255)
CERVENA = (255, 0, 0)

# Písma
import pygame
pygame.font.init()
FONT = pygame.font.Font(None, 72)
MALY_FONT = pygame.font.Font(None, 36)
