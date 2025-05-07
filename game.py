import random
import time
from config import *
from graphics import draw_board, otoc_animaciu, nacitaj_obrazok
import sounds
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
            rect = pygame.Rect(col * VELKOST_KARTY, row * VELKOST_KARTY, VELKOST_KARTY, VELKOST_KARTY)
            rub_img = pygame.image.load("assets/obrazky/back.png")
            rub_img = pygame.transform.scale(rub_img, (VELKOST_KARTY - 5, VELKOST_KARTY - 5))
            lice_img = nacitaj_obrazok(self.karty[index])
            otoc_animaciu(self.screen, rect, rub_img, lice_img)

            self.odhalene[index] = True
            sounds.flip_sound.play()
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
            sounds.match_sound.play()
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

        while hra_bezi:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)

            if self.je_koniec():
                spat_rect, nova_hra_rect = zobraz_gameover(self.screen, self.skore)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return False
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if spat_rect.collidepoint(event.pos):
                                return True
                            elif nova_hra_rect.collidepoint(event.pos):
                                self.__init__(self.screen)
                                break
                    else:
                        pygame.time.delay(100)
                        continue
                    break

        return True
