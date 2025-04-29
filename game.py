import pygame
import random
import time
from config import *
from graphics import draw_board

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.karty = [
            "banan.jpg", "banan.jpg",
            "brusnica.png", "brusnica.png",
            "citron.jpg", "citron.jpg",
            "jablko.jpg", "jablko.jpg",
            "jahoda.jpg", "jahoda.jpg",
            "kiwi.jpg", "kiwi.jpg",
            "pomaranc.jpg", "pomaranc.jpg",
            "visne.jpg", "visne.jpg"
        ]
        random.shuffle(self.karty)
        self.odhalene = [False] * len(self.karty)
        self.otocene = []
        self.spojene = []
        self.hrac_narade = 1
        self.skore = {1: 0, 2: 0}

    def draw(self):
        draw_board(self.screen, self.karty, self.odhalene, self.spojene,
                   self.hrac_narade, self.skore)

    def handle_click(self, pos):
        x, y = pos
        row = y // VELKOST_KARTY
        col = x // VELKOST_KARTY
        index = row * VELKOST_POLA + col
        if 0 <= index < len(self.karty) and not self.odhalene[index] and index not in self.spojene:
            self.odhalene[index] = True
            self.otocene.append(index)
            if len(self.otocene) == 2:
                self.kontrola()

    def kontrola(self):
        i, j = self.otocene
        self.draw()
        pygame.display.update()
        time.sleep(1.5)
        if self.karty[i] == self.karty[j]:
            self.spojene.extend(self.otocene)
            self.skore[self.hrac_narade] += 1
        else:
            self.odhalene[i] = False
            self.odhalene[j] = False
            self.hrac_narade = 2 if self.hrac_narade == 1 else 1
        self.otocene = []

    def je_koniec(self):
        return len(self.spojene) == len(self.karty)

    def zobraz_vysledok(self):
        self.screen.fill(BIELA)
        vysledok_text = FONT.render("Koniec hry!", True, CIERNA)
        self.screen.blit(vysledok_text, (WIDTH // 2 - vysledok_text.get_width() // 2, 100))

        skore1 = MALY_FONT.render(f"Hráč 1: {self.skore[1]} bodov", True, MODRA)
        skore2 = MALY_FONT.render(f"Hráč 2: {self.skore[2]} bodov", True, CERVENA)

        self.screen.blit(skore1, (WIDTH // 2 - skore1.get_width() // 2, 200))
        self.screen.blit(skore2, (WIDTH // 2 - skore2.get_width() // 2, 250))

        tlacidlo_rect = pygame.Rect(WIDTH // 2 - 100, 350, 200, 60)
        pygame.draw.rect(self.screen, SIVA, tlacidlo_rect)
        text = MALY_FONT.render("Späť", True, CIERNA)
        self.screen.blit(text, (tlacidlo_rect.centerx - text.get_width() // 2,
                                tlacidlo_rect.centery - text.get_height() // 2))

        pygame.display.flip()
        return tlacidlo_rect
