import pygame
import config

background_image = pygame.transform.scale(
    pygame.image.load('assets/obrazky/pexeso.png'),
    (config.WIDTH, config.HEIGHT)
)

def zobraz_obtiaznosti(screen):
    running = True

    while running:
        screen.blit(background_image, (0, 0))

        nadpis = config.FONT.render("Vyber obtiažnosť", True, config.CIERNA)
        screen.blit(nadpis, (config.WIDTH // 2 - nadpis.get_width() // 2, 80))

        font = config.MALY_FONT
        farba = config.SIVA

        lahka_rect = pygame.Rect(config.WIDTH // 2 - 100, 180, 200, 60)
        pygame.draw.rect(screen, farba, lahka_rect)
        text_lahka = font.render("Ľahká", True, config.CIERNA)
        screen.blit(text_lahka, (lahka_rect.centerx - text_lahka.get_width() // 2,
                                 lahka_rect.centery - text_lahka.get_height() // 2))

        stredna_rect = pygame.Rect(config.WIDTH // 2 - 100, 270, 200, 60)
        pygame.draw.rect(screen, farba, stredna_rect)
        text_stredna = font.render("Stredná", True, config.CIERNA)
        screen.blit(text_stredna, (stredna_rect.centerx - text_stredna.get_width() // 2,
                                   stredna_rect.centery - text_stredna.get_height() // 2))

        tazka_rect = pygame.Rect(config.WIDTH // 2 - 100, 360, 200, 60)
        pygame.draw.rect(screen, farba, tazka_rect)
        text_tazka = font.render("Ťažká", True, config.CIERNA)
        screen.blit(text_tazka, (tazka_rect.centerx - text_tazka.get_width() // 2,
                                 tazka_rect.centery - text_tazka.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if stredna_rect.collidepoint(event.pos):
                    return "stredna"
                elif lahka_rect.collidepoint(event.pos):
                    print("Ľahká obtiažnosť ešte nie je implementovaná.")
                elif tazka_rect.collidepoint(event.pos):
                    print("Ťažká obtiažnosť ešte nie je implementovaná.")
