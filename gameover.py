import pygame
from config import *


def zobraz_gameover(screen, skore):
    screen.fill(BIELA)
    vysledok_text = FONT.render("Koniec hry!", True, CIERNA)
    screen.blit(vysledok_text, (WIDTH // 2 - vysledok_text.get_width() // 2, 100))

    skore1 = MALY_FONT.render(f"Hráč 1: {skore[1]} bodov", True, MODRA)
    skore2 = MALY_FONT.render(f"Hráč 2: {skore[2]} bodov", True, CERVENA)

    screen.blit(skore1, (WIDTH // 2 - skore1.get_width() // 2, 200))
    screen.blit(skore2, (WIDTH // 2 - skore2.get_width() // 2, 250))

    tlacidlo_rect = pygame.Rect(WIDTH // 2 - 100, 350, 200, 60)
    pygame.draw.rect(screen, SIVA, tlacidlo_rect)
    text = MALY_FONT.render("Späť", True, CIERNA)
    screen.blit(text, (tlacidlo_rect.centerx - text.get_width() // 2,
                       tlacidlo_rect.centery - text.get_height() // 2))

    pygame.display.flip()
    return tlacidlo_rect

