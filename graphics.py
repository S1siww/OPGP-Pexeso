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
    screen.blit(na_rade_text, (WIDTH // 2 - 270, VELKOST_POLA * VELKOST_KARTY + 10))

    skore_text1 = MALY_FONT.render(f"Body - Hráč 1: {skore[1]}", True, CIERNA)
    screen.blit(skore_text1, (WIDTH // 2 - 30, VELKOST_POLA * VELKOST_KARTY + 10))

    skore_text2 = MALY_FONT.render(f"Hráč 2: {skore[2]}", True, CIERNA)
    screen.blit(skore_text2, (WIDTH // 2 + 53, VELKOST_POLA * VELKOST_KARTY + 50))
    

    pygame.display.flip()
