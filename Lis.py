from Zwierze import Zwierze
import numpy.random as nrand

class Lis(Zwierze):
    def __init__(self, polozenie, swiat): #    def __init__(self, polozenie, swiat):
        self.sila = 3
        self.ini = 7
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Lis'
        self.kolor = (255, 100, 20)
        print(f"{self.gatunek} {self.polozenie} stworzony")

    def akcja(self):
        print(self.get_gatunek(), self.get_polozenie(), "przemieszcza się na", end=' ')
        walka = False
        ruch = [0, 0]
        kierunek = nrand.randint(0,4)
        if kierunek == 0:
            ruch[0] += 1
        elif kierunek == 1:
            ruch[0] -= 1
        elif kierunek == 2:
            ruch[1] += 1
        elif kierunek == 3:
            ruch[1] -= 1
        #jesli pole miesci sie w wymiarach swiata i organizm na tym polu nie uniemozliwil ruchu
        if self.swiat.sprawdz_granice([self.polozenie[0]+ruch[0], self.polozenie[1]+ruch[1]]):
            kolidujacy = self.swiat.znajdz_organizm([self.polozenie[0]+ruch[0], self.polozenie[1]+ruch[1]], None)
            if kolidujacy == None:
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]
            elif kolidujacy.kolizja(self) == False and kolidujacy.get_sila()<=self.sila:
                walka = True
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]
                self.swiat.walka(self, kolidujacy)
        if walka == True:
            print(self.get_polozenie(), "// kolizja!")
        else:
            print(self.get_polozenie())