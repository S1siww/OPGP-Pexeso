from config import *


def zobraz_menu(screen):
    running = True

    while running:
        screen.fill(BIELA)

        title_text = FONT.render("Pexeso", True, CIERNA)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 80))

        lokalne_rect = pygame.Rect(WIDTH // 2 - 100, 200, 200, 60)
        pygame.draw.rect(screen, MODRA, lokalne_rect)
        lokalne_text = MALY_FONT.render("Hrať lokálne", True, BIELA)
        screen.blit(lokalne_text, (lokalne_rect.x + 30, lokalne_rect.y + 15))

        online_rect = pygame.Rect(WIDTH // 2 - 100, 280, 200, 60)
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
