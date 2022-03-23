from Zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self, polozenie, swiat): #    def __init__(self, polozenie, swiat):
        self.sila = 4
        self.ini = 4
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Owca'
        self.kolor = (190, 190, 190)
        print(f"{self.gatunek} {self.polozenie} stworzony")