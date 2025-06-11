import pygame
import config

VELKOST_KARTY = config.VELKOST_KARTY
VELKOST_POLA = config.VELKOST_POLA
WIDTH = VELKOST_KARTY * VELKOST_POLA
HEIGHT = VELKOST_KARTY * VELKOST_POLA + 100

BIELA = (255, 255, 255)
CIERNA = (0, 0, 0)
MODRA = (0, 102, 204)
CERVENA = (204, 0, 0)
SIVA = (160, 160, 160)

pygame.font.init()
MALY_FONT = pygame.font.SysFont("Arial", 25)

back_img = pygame.image.load("assets/obrazky/back.png")
back_img = pygame.transform.scale(back_img, (VELKOST_KARTY - 5, VELKOST_KARTY - 5))


def nacitaj_obrazok(nazov):
    obrazok = pygame.image.load(f"assets/obrazky/{nazov}")
    return pygame.transform.scale(obrazok, (VELKOST_KARTY - 5, VELKOST_KARTY - 5))


def draw_board(screen, karty, odhalene, spojene, hrac_narade, skore, vyherne_karty):
    screen.fill(BIELA)
    for i in range(VELKOST_POLA):
        for j in range(VELKOST_POLA):
            index = i * VELKOST_POLA + j
            x, y = j * VELKOST_KARTY, i * VELKOST_KARTY

            if index in spojene:
                farba = MODRA if vyherne_karty.get(index) == 1 else CERVENA
            else:
                farba = SIVA

            pygame.draw.rect(screen, farba, (x, y, VELKOST_KARTY - 5, VELKOST_KARTY - 5))

            if odhalene[index] or index in spojene:
                image = pygame.image.load(f"assets/obrazky/{karty[index]}")
                image = pygame.transform.scale(image, (VELKOST_KARTY - 5, VELKOST_KARTY - 5))
                screen.blit(image, (x + 5, y + 5))
            else:
                screen.blit(back_img, (x + 5, y + 5))

    na_rade_text = MALY_FONT.render(f"Na rade je {hrac_narade}. hráč", True, MODRA if hrac_narade == 1 else CERVENA)
    screen.blit(na_rade_text, (WIDTH // 2 - 270, VELKOST_POLA * VELKOST_KARTY + 10))

    skore_text1 = MALY_FONT.render(f"Body - Hráč 1: {skore[1]}", True, CIERNA)
    screen.blit(skore_text1, (WIDTH // 2 - 30, VELKOST_POLA * VELKOST_KARTY + 10))

    skore_text2 = MALY_FONT.render(f"Hráč 2: {skore[2]}", True, CIERNA)
    screen.blit(skore_text2, (WIDTH // 2 + 53, VELKOST_POLA * VELKOST_KARTY + 50))

    pygame.display.flip()


def otoc_animaciu(screen, rect, obrazok1, obrazok2):
    for scale in range(VELKOST_KARTY, 0, -20):
        zmenseny = pygame.transform.scale(obrazok1, (scale, VELKOST_KARTY - 5))
        screen.blit(zmenseny, (rect.x + (VELKOST_KARTY - scale) // 2, rect.y + 5))
        pygame.display.flip()
        pygame.time.wait(10)

    for scale in range(0, VELKOST_KARTY, 20):
        zmenseny = pygame.transform.scale(obrazok2, (scale, VELKOST_KARTY - 5))
        screen.blit(zmenseny, (rect.x + (VELKOST_KARTY - scale) // 2, rect.y + 5))
        pygame.display.flip()
        pygame.time.wait(10)
