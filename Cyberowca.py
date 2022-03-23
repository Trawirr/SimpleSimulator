from Zwierze import Zwierze
import numpy.random as nrand

class Cyberowca(Zwierze):
    def __init__(self, polozenie, swiat): #    def __init__(self, polozenie, swiat):
        self.sila = 11
        self.ini = 4
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Cyberowca'
        self.kolor = (0, 0, 220)
        print(f"{self.gatunek} {self.polozenie} stworzony")

    def akcja(self):
        print(self.get_gatunek(), self.get_polozenie(), "przemieszcza się na", end=' ')
        organizmy = self.swiat.get_organizmy()
        znaleziony = False
        walka = False
        d = self.swiat.get_rozmiar()**2
        ruch = [0, 0]
        p = [0, 0]
        # szukanie najblizszego barszczu
        for organizm in organizmy:
            if organizm.get_gatunek() == "Barszcz":
                znaleziony = True
                x, y = organizm.get_polozenie()
                if (self.polozenie[0] - x)**2 + (self.polozenie[1] - y)**2 < d:
                    p = [x, y]

        if znaleziony == True:
            if p[0] > self.polozenie[0]:
                ruch = [1, 0]
            elif p[0] < self.polozenie[0]:
                ruch = [-1, 0]
            elif p[0] == self.polozenie[0]:
                if p[1] > self.polozenie[1]:
                    ruch = [0, 1]
                elif p[1] < self.polozenie[1]:
                    ruch = [0, -1]
        else:
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
        # jesli pole miesci sie w wymiarach swiata i organizm na tym polu nie uniemozliwil ruchu
        if self.swiat.sprawdz_granice([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]):
            kolidujacy = self.swiat.znajdz_organizm([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]],
                                                    None)
            if kolidujacy == None:
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]
            elif kolidujacy.kolizja(self) == False:
                walka = True
                if kolidujacy.get_gatunek() == "Barszcz:":
                    self.swiat.usun_organizm(kolidujacy)
                else:
                    self.swiat.walka(self, kolidujacy)
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]
        if walka == True:
            print([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]], "// kolizja!")
        else:
            print([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]])

