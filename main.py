import pygame
from config import WIDTH, HEIGHT
from game import Game
from menu import zobraz_menu
import gameover
from difficulty import zobraz_obtiaznosti



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pexeso")

    running = True

    while running:
        zobraz_menu(screen)
        volba = zobraz_obtiaznosti(screen)
        if volba == "stredna":
            game = Game(screen)
        else: 
            continue

        hra_bezi = True
        while hra_bezi:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    hra_bezi = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    game.klik(event.pos)

            game.draw()

            if game.vyhodnotenie():
                pygame.time.wait(1000)
                spat_rect, nova_hra_rect = gameover.zobraz_gameover(screen, game.skore)

                vyber = None
                while vyber is None:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            vyber = "koniec"
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if spat_rect.collidepoint(event.pos):
                                vyber = "menu"
                            elif nova_hra_rect.collidepoint(event.pos):
                                vyber = "nova_hra"

                    pygame.time.delay(100)

                if vyber == "koniec":
                    running = False
                    hra_bezi = False
                elif vyber == "menu":
                    hra_bezi = False
                elif vyber == "nova_hra":
                    volba = zobraz_obtiaznosti(screen)
                    if volba == "stredna":
                        game = Game(screen)
                    else:
                        hra_bezi = False


    pygame.quit()


if __name__ == "__main__":
    main()
