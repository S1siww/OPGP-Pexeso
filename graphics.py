from config import *
import pygame

back_img = pygame.image.load("assets/obrazky/back.png")
back_img = pygame.transform.scale(back_img, (VELKOST_KARTY - 5, VELKOST_KARTY - 5))


def draw_board(screen, karty, odhalene, spojene, hrac_narade, skore):
    screen.fill(BIELA)
    for i in range(VELKOST_POLA):
        for j in range(VELKOST_POLA):
            index = i * VELKOST_POLA + j
            x, y = j * VELKOST_KARTY, i * VELKOST_KARTY

            pygame.draw.rect(screen, SIVA, (x, y, VELKOST_KARTY - 5, VELKOST_KARTY - 5))

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


def nacitaj_obrazok(nazov):
    image = pygame.image.load(f"assets/obrazky/{nazov}")
    return pygame.transform.scale(image, (VELKOST_KARTY - 5, VELKOST_KARTY - 5))


def otoc_animaciu(screen, rect, rub_img, lice_img):
    for scale in range(VELKOST_KARTY - 5, 0, -20):
        scaled = pygame.transform.scale(rub_img, (scale, rect.height - 5))
        x = rect.centerx - scaled.get_width() // 2
        y = rect.y + 5
        screen.fill(BIELA, rect)
        screen.blit(scaled, (x, y))
        pygame.display.update(rect)
        pygame.time.delay(20)

    for scale in range(0, VELKOST_KARTY - 4, 20):
        scaled = pygame.transform.scale(lice_img, (scale, rect.height - 5))
        x = rect.centerx - scaled.get_width() // 2
        y = rect.y + 5
        screen.fill(BIELA, rect)
        screen.blit(scaled, (x, y))
        pygame.display.update(rect)
        pygame.time.delay(20)
