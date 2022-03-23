from Organizm import Organizm
import Swiat
import numpy.random as nrand
import pygame


class Zwierze(Organizm):
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
            elif kolidujacy.kolizja(self) == False:
                walka = True
                self.polozenie = [self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]
                self.swiat.walka(self, kolidujacy)
        if walka == True:
            print([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]], "// kolizja!")
        else:
            print([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]])



    def kolizja(self, organizm):
        # dwa takie same gatunki moga sie rozmnozyc
        if organizm.get_gatunek() == self.gatunek and nrand.randint(0, 100) < 20:
            for ruch in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                polozenie = [self.polozenie[0]+ruch[0], self.polozenie[1]+ruch[1]]
                if self.swiat.znajdz_organizm(polozenie, None) == None:
                    self.swiat.dodaj_po_gatunku(polozenie, self.get_gatunek())
                    break
            return True
        else:
            return False

    def get_ini(self):
        return self.ini

    def get_polozenie(self):
        return self.polozenie

    def get_sila(self):
        return self.sila

    def get_gatunek(self):
        return self.gatunek

    def set_sila(self, nowa_sila):
        self.sila = nowa_sila

    def rysowanie(self):
        d = 25
        i = self.polozenie[0]
        j = self.polozenie[1]

        pygame.draw.rect(self.swiat.get_okno(), self.kolor, (i*d+1,j*d+1, d-1, d-1))