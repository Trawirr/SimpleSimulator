from Zwierze import Zwierze
import numpy.random as nrand

class Antylopa(Zwierze):
    def __init__(self, polozenie, swiat): #    def __init__(self, polozenie, swiat):
        self.sila = 4
        self.ini = 4
        self.polozenie = polozenie
        self.swiat = swiat
        self.gatunek = 'Antylopa'
        self.kolor = (240, 180, 110)
        print(f"{self.gatunek} {self.polozenie} stworzony")

    def akcja(self):
        walka = False
        print(self.get_gatunek(), self.get_polozenie(), "przemieszcza się na", end=' ')
        ruch = [0, 0]
        for i in range(2):
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
                                                    self)
            if kolidujacy == None:
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]

            elif kolidujacy.kolizja(self) == False:
                walka = True
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]
                self.swiat.walka(self, kolidujacy)

        if walka == True:
            print(self.get_polozenie(), "// kolizja!")
        else:
            print(self.get_polozenie())

    def kolizja(self, organizm):
        # z prawdopodobienstem 50% antylopa przechodzi na sasiednie niezajete pole
        for ruch in [[1,0], [-1,0], [0,1], [0,-1]]:
            if self.swiat.sprawdz_granice([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]) and self.swiat.znajdz_organizm([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]], self) == None:
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]
                return True
        return False