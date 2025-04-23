import pygame
from config import *


def draw_board(screen, karty, odhalene, spojene, hrac_narade, skore):
    screen.fill(BIELA)
    for i in range(VELKOST_POLA):
        for j in range(VELKOST_POLA):
            index = i * VELKOST_POLA + j
            x, y = j * VELKOST_KARTY, i * VELKOST_KARTY
            pygame.draw.rect(screen, SIVA, (x, y, VELKOST_KARTY - 5, VELKOST_KARTY - 5))

            if odhalene[index] or index in spojene:
                image = pygame.image.load(f"assets/{karty[index]}")
                image = pygame.transform.scale(image, (VELKOST_KARTY - 5, VELKOST_KARTY - 5))
                screen.blit(image, (x + 5, y + 5))

    na_rade_text = MALY_FONT.render(f"Na rade je {hrac_narade}. hráč", True, MODRA if hrac_narade == 1 else CERVENA)
    screen.blit(na_rade_text, (20, HEIGHT - 50))

    skore_text = MALY_FONT.render(f"Body - Hráč 1: {skore[1]}  Hráč 2: {skore[2]}", True, CIERNA)
    screen.blit(skore_text, (WIDTH // 2 - 60, HEIGHT - 50))

    pygame.display.flip()
