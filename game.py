import pygame
import random
import time
import config
import graphics
import sounds


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.karty = config.KARTY.copy()
        random.shuffle(self.karty)
        self.odhalene = [False] * len(self.karty)
        self.otocene = []
        self.spojene = []
        self.hrac_narade = 1
        self.skore = {1: 0, 2: 0}
        self.vyherne_karty = {}  # index: hráč

    def klik(self, pozicia):
        x, y = pozicia
        stlpec = x // config.VELKOST_KARTY
        riadok = y // config.VELKOST_KARTY
        index = riadok * config.VELKOST_POLA + stlpec

        if not self.odhalene[index] and index not in self.spojene and len(self.otocene) < 2:
            self.odhalene[index] = True
            self.otocene.append(index)

        if len(self.otocene) == 2:
            self.kontrola()

    def kontrola(self):
        i, j = self.otocene
        self.draw()
        pygame.display.update()
        time.sleep(0.5)

        if self.karty[i] == self.karty[j]:
            self.spojene.extend(self.otocene)
            self.vyherne_karty[i] = self.hrac_narade
            self.vyherne_karty[j] = self.hrac_narade
            sounds.match_sound.play()
            self.skore[self.hrac_narade] += 1
        else:
            for index in (i, j):
                row = index // config.VELKOST_POLA
                col = index % config.VELKOST_POLA
                rect = pygame.Rect(col * config.VELKOST_KARTY, row * config.VELKOST_KARTY,
                                   config.VELKOST_KARTY, config.VELKOST_KARTY)
                lice_img = graphics.nacitaj_obrazok(self.karty[index])
                rub_img = graphics.nacitaj_obrazok("back.png")
                graphics.otoc_animaciu(self.screen, rect, lice_img, rub_img)

            self.odhalene[i] = False
            self.odhalene[j] = False
            self.hrac_narade = 2 if self.hrac_narade == 1 else 1

        self.otocene = []

    def draw(self):
        graphics.draw_board(self.screen, self.karty, self.odhalene, self.spojene,
                            self.hrac_narade, self.skore, self.vyherne_karty)

    def vyhodnotenie(self):
        if len(self.spojene) == len(self.karty):
            return True
        return False
