import pygame
from config import WIDTH, HEIGHT
from game import Game
from menu import zobraz_menu
from gameover import zobraz_gameover


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pexeso")

    running = True
    while running:
        zobraz_menu(screen)

        game = Game(screen)
        hra_bezi = True

        while hra_bezi:
            game.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hra_bezi = False
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    game.handle_click(event.pos)

            if game.je_koniec():
                tlacidlo_rect = zobraz_gameover(screen, game.skore)
                cakanie = True
                while cakanie:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            cakanie = False
                            hra_bezi = False
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if tlacidlo_rect.collidepoint(event.pos):
                                cakanie = False
                                hra_bezi = False
                    pygame.time.delay(100)

    pygame.quit()


if __name__ == "__main__":
    main()
