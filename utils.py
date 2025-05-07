import random


def nova_hra():
    karty = list("AABBCCDDEEFFGGHH")
    random.shuffle(karty)
    return {
        "karty": karty,
        "odhalene": [False] * len(karty),
        "spojene": [],
        "otocene": [],
        "hrac_narade": 1,
        "skore": {1: 0, 2: 0}
    }


def zmen_hraca(hrac):
    return 2 if hrac == 1 else 2


def hra_skoncila(spojene, pocet_kariet):
    return len(spojene) == pocet_kariet


def resetuj_hru(self):
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

