import pygame
import config

background_image = pygame.transform.scale(
    pygame.image.load('assets/obrazky/back.png'), 
    (config.WIDTH, config.HEIGHT)
)

def zobraz_gameover(screen, skore):
    bg_x = (config.WIDTH - background_image.get_width()) // 2
    bg_y = (config.HEIGHT - background_image.get_height()) // 2
    screen.blit(background_image, (bg_x, bg_y))

    vysledok_text = config.FONT.render("Koniec hry!", True, config.CIERNA)
    screen.blit(vysledok_text, (config.WIDTH // 2 - vysledok_text.get_width() // 2, 180))

    skore1 = config.MALY_FONT.render(f"Hráč 1: {skore[1]} bodov", True, config.MODRA)
    skore2 = config.MALY_FONT.render(f"Hráč 2: {skore[2]} bodov", True, config.CERVENA)

    screen.blit(skore1, (config.WIDTH // 2 - skore1.get_width() // 2, 250))
    screen.blit(skore2, (config.WIDTH // 2 - skore2.get_width() // 2, 290))

    if skore[1] > skore[2]:
        vitaz_text = config.MALY_FONT.render("Vyhral hráč 1!", True, config.MODRA)
    elif skore[2] > skore[1]:
        vitaz_text = config.MALY_FONT.render("Vyhral hráč 2!", True, config.CERVENA)
    else:
        vitaz_text = config.MALY_FONT.render("Remíza!", True, config.CIERNA)

    screen.blit(vitaz_text, (config.WIDTH // 2 - vitaz_text.get_width() // 2, 340))

    spat = pygame.transform.scale(pygame.image.load('assets/obrazky/spat.png'), (config.WIDTH, config.HEIGHT))
    spat = pygame.transform.smoothscale(spat, (300, 250))
    spat_rect = spat.get_rect(center=(config.WIDTH // 2, 370)) 
    screen.blit(spat, (spat_rect.x + 5, spat_rect.y - 10))

    nova_hra = pygame.transform.scale(pygame.image.load('assets/obrazky/novahra.png'), (config.WIDTH, config.HEIGHT))
    nova_hra = pygame.transform.smoothscale(nova_hra, (300, 250))
    nova_hra_rect = nova_hra.get_rect(center=(config.WIDTH // 2, 470)) 
    screen.blit(nova_hra, (nova_hra_rect.x + 5, nova_hra_rect.y - 10))

    pygame.display.flip()

    return spat_rect, nova_hra_rect
