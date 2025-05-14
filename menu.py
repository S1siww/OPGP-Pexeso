import pygame
import config

background_image = pygame.transform.scale(
    pygame.image.load('assets/obrazky/pexeso.png'),
    (config.WIDTH, config.HEIGHT)
)

def zobraz_menu(screen):
    running = True

    while running:
        bg_x = (config.WIDTH - background_image.get_width()) // 2
        bg_y = (config.HEIGHT - background_image.get_height()) // 2
        screen.blit(background_image, (bg_x, bg_y))

        lokalne = pygame.transform.scale(pygame.image.load('assets/obrazky/hratlokalne.png'), (config.WIDTH, config.HEIGHT))
        lokalne = pygame.transform.smoothscale(lokalne, (300, 250))
        lokalne_rect = lokalne.get_rect(center=(config.WIDTH // 2, 350)) 
        screen.blit(lokalne, (lokalne_rect.x + 5, lokalne_rect.y - 10))

        online = pygame.transform.scale(pygame.image.load('assets/obrazky/hratonline.png'), (config.WIDTH, config.HEIGHT))
        online = pygame.transform.smoothscale(online, (300, 250))
        online_rect = online.get_rect(center=(config.WIDTH // 2, 440)) 
        screen.blit(online, (online_rect.x + 5, online_rect.y - 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if lokalne_rect.collidepoint(event.pos):
                    return
