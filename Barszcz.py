from Roslina import Roslina
import numpy.random as nrand

class Barszcz(Roslina):
    def __init__(self, polozenie, swiat):
        self.sila = 10
        self.ini = 0
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Barszcz'
        self.kolor = (255, 0, 0)
        print(f"{self.gatunek} {self.polozenie} stworzony")

    def akcja(self):
        for ruch in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            kolidujacy = self.swiat.znajdz_organizm([self.polozenie[0]+ruch[0], self.polozenie[1]+ruch[1]], None)
            if kolidujacy != None:
                if kolidujacy.get_gatunek() != "Cyberowca":
                    self.swiat.usun_organizm(kolidujacy)