from config import *
background_image = pygame.transform.scale(pygame.image.load('assets/obrazky/pexeso.png'), (WIDTH, HEIGHT))


def zobraz_menu(screen):
    running = True

    while running:
        bg_x = (WIDTH - background_image.get_width()) // 2
        bg_y = (HEIGHT - background_image.get_height()) // 2
        screen.blit(background_image, (bg_x, bg_y))


        lokalne_rect = pygame.Rect(WIDTH // 2 - 100, 410, 200, 60)
        pygame.draw.rect(screen, MODRA, lokalne_rect)
        lokalne_text = MALY_FONT.render("Hrať lokálne", True, BIELA)
        screen.blit(lokalne_text, (lokalne_rect.x + 30, lokalne_rect.y + 15))

        online_rect = pygame.Rect(WIDTH // 2 - 100, 480, 200, 60)
        pygame.draw.rect(screen, SIVA, online_rect)
        online_text = MALY_FONT.render("Online (WIP)", True, CIERNA)
        screen.blit(online_text, (online_rect.x + 20, online_rect.y + 15))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if lokalne_rect.collidepoint(event.pos):
                    return
