import pygame
from config import WIDTH, HEIGHT
from game import Game
from menu import zobraz_menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pexeso")

    running = True
    while running:
        zobraz_menu(screen)
        game = Game(screen)
        running = game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
