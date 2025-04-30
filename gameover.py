import pygame
from config import WIDTH, BIELA, CIERNA, SIVA, FONT, MALY_FONT, MODRA, CERVENA

def zobraz_gameover(screen, skore):
    screen.fill(BIELA)

    # Nadpis
    vysledok_text = FONT.render("Koniec hry!", True, CIERNA)
    screen.blit(vysledok_text, (WIDTH // 2 - vysledok_text.get_width() // 2, 80))

    # Skóre hráčov
    skore1 = MALY_FONT.render(f"Hráč 1: {skore[1]} bodov", True, MODRA)
    skore2 = MALY_FONT.render(f"Hráč 2: {skore[2]} bodov", True, CERVENA)

    screen.blit(skore1, (WIDTH // 2 - skore1.get_width() // 2, 150))
    screen.blit(skore2, (WIDTH // 2 - skore2.get_width() // 2, 190))

    # Výherca alebo remíza
    if skore[1] > skore[2]:
        vitaz_text = MALY_FONT.render("Vyhral hráč 1!", True, MODRA)
    elif skore[2] > skore[1]:
        vitaz_text = MALY_FONT.render("Vyhral hráč 2!", True, CERVENA)
    else:
        vitaz_text = MALY_FONT.render("Remíza!", True, CIERNA)

    screen.blit(vitaz_text, (WIDTH // 2 - vitaz_text.get_width() // 2, 240))

    # Tlačidlo "Späť"
    tlacidlo_rect = pygame.Rect(WIDTH // 2 - 100, 320, 200, 60)
    pygame.draw.rect(screen, SIVA, tlacidlo_rect)
    text = MALY_FONT.render("Späť", True, CIERNA)
    screen.blit(text, (tlacidlo_rect.centerx - text.get_width() // 2,
                       tlacidlo_rect.centery - text.get_height() // 2))

    pygame.display.flip()
    return tlacidlo_rect
