from Zwierze import Zwierze

class Zolw(Zwierze):
    def __init__(self, polozenie, swiat): #    def __init__(self, polozenie, swiat):
        self.sila = 2
        self.ini = 1
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Zolw'
        self.kolor = (70, 205, 105)
        print(f"{self.gatunek} {self.polozenie} stworzony")

    def kolizja(self, organizm):
        if organizm.get_sila() < 5:
            return True
        else:
            return False