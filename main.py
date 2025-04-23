import pygame
from config import WIDTH, HEIGHT
from game import Game
from graphics import draw_board

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pexeso")

    game = Game(screen)

    running = True
    while running:
        game.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.handle_click(event.pos)

    pygame.quit()

if __name__ == "__main__":
    main()
