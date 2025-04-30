import pygame
import random
import time
from config import *
from graphics import draw_board
from gameover import zobraz_gameover


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
        time.sleep(0.5)
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

    def run(self):
        hra_bezi = True
        running = True

        while hra_bezi:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hra_bezi = False
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)

            if self.je_koniec():
                tlacidlo_rect = zobraz_gameover(self.screen, self.skore)
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

        return running
