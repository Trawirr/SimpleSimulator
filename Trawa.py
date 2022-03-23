from Roslina import Roslina
import numpy.random as nrand

class Trawa(Roslina):
    def __init__(self, polozenie, swiat):
        self.sila = 0
        self.ini = 0
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Trawa'
        self.kolor = (153, 255, 153)
        print(f"{self.gatunek} {self.polozenie} stworzony")

    def akcja(self):
        szansa = 25
        ruch = [0, 0]
        kierunek = nrand.randint(0, 4)
        if kierunek == 0:
            ruch[0] += 1
        elif kierunek == 1:
            ruch[0] -= 1
        elif kierunek == 2:
            ruch[1] += 1
        elif kierunek == 3:
            ruch[1] -= 1
        if nrand.randint(0,100) < szansa:
            print(self.get_gatunek(), self.get_polozenie(), "rozsiewa się na", end=' ')
            if self.swiat.sprawdz_granice([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]) and self.swiat.znajdz_organizm([self.polozenie[0]+ruch[0], self.polozenie[1]+ruch[1]], None) == None:
                self.swiat.dodaj_organizm(Trawa([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]], self.swiat))
            print([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]])
        else:
            print(self.get_gatunek(), self.get_polozenie(), "nie rozsiewa się")