from Zwierze import Zwierze

class Wilk(Zwierze):
    def __init__(self, polozenie, swiat): #    def __init__(self, polozenie, swiat):
        self.sila = 9
        self.ini = 5
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Wilk'
        self.kolor = (100, 85, 60)
        print(f"{self.gatunek} {self.polozenie} stworzony")