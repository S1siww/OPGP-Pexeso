import pygame
from config import WIDTH, HEIGHT
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pexeso")

    game = Game(screen)
    running = True
    koniec = False

    while running:
        if not koniec:
            game.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    game.handle_click(event.pos)
                    if game.je_koniec():
                        koniec = True
        else:
            tlacidlo = game.zobraz_vysledok()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if tlacidlo.collidepoint(event.pos):
                        game = Game(screen)
                        koniec = False

    pygame.quit()

if __name__ == "__main__":
    main()
