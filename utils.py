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

