import pygame
import config

background_image = pygame.transform.scale(
    pygame.image.load('assets/obrazky/pexeso.png'), 
    (config.WIDTH, config.HEIGHT)
)

def zobraz_gameover(screen, skore):
    bg_x = (config.WIDTH - background_image.get_width()) // 2
    bg_y = (config.HEIGHT - background_image.get_height()) // 2
    screen.blit(background_image, (bg_x, bg_y))

    vysledok_text = config.FONT.render("Koniec hry!", True, config.CIERNA)
    screen.blit(vysledok_text, (config.WIDTH // 2 - vysledok_text.get_width() // 2, 80))

    skore1 = config.MALY_FONT.render(f"Hráč 1: {skore[1]} bodov", True, config.MODRA)
    skore2 = config.MALY_FONT.render(f"Hráč 2: {skore[2]} bodov", True, config.CERVENA)

    screen.blit(skore1, (config.WIDTH // 2 - skore1.get_width() // 2, 150))
    screen.blit(skore2, (config.WIDTH // 2 - skore2.get_width() // 2, 190))

    if skore[1] > skore[2]:
        vitaz_text = config.MALY_FONT.render("Vyhral hráč 1!", True, config.MODRA)
    elif skore[2] > skore[1]:
        vitaz_text = config.MALY_FONT.render("Vyhral hráč 2!", True, config.CERVENA)
    else:
        vitaz_text = config.MALY_FONT.render("Remíza!", True, config.CIERNA)

    screen.blit(vitaz_text, (config.WIDTH // 2 - vitaz_text.get_width() // 2, 240))

    spat_rect = pygame.Rect(config.WIDTH // 2 - 100, 320, 200, 60)
    pygame.draw.rect(screen, config.SIVA, spat_rect)
    text = config.MALY_FONT.render("Späť", True, config.CIERNA)
    screen.blit(text, (spat_rect.centerx - text.get_width() // 2,
                       spat_rect.centery - text.get_height() // 2))

    nova_hra_rect = pygame.Rect(config.WIDTH // 2 - 100, 400, 200, 60)
    pygame.draw.rect(screen, config.SIVA, nova_hra_rect)
    nova_hra_text = config.MALY_FONT.render("Nová hra", True, config.CIERNA)
    screen.blit(nova_hra_text, (nova_hra_rect.centerx - nova_hra_text.get_width() // 2,
                                nova_hra_rect.centery - nova_hra_text.get_height() // 2))

    pygame.display.flip()

    return spat_rect, nova_hra_rect
