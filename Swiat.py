import numpy.random as nrand
import pygame
import Organizm
from time import sleep
import Antylopa
import Barszcz
import Cyberowca
import Czlowiek
import Guarana
import Lis
import Mlecz
import Owca
import Trawa
import WilczeJagody
import Wilk
import Zolw

class Swiat:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
        self.organizmy = []
        self.okno = pygame.display.set_mode((rozmiar*25, rozmiar*25))
        print(f"Stworzono swiat o wymiarach {rozmiar}x{rozmiar}")

        # dodawanie losowych poczatkowych organizmow
        self.dodaj_organizm(Czlowiek.Czlowiek([self.rozmiar//2, self.rozmiar//2], self))
        nazwy = ('Antylopa', 'Barszcz', 'Cyberowca', 'Guarana', 'Lis', 'Mlecz',
                 'Owca', 'Trawa', 'Wilcze jagody', 'Wilk', 'Zolw')
        for i in range(rozmiar*2):
            polozenie = [nrand.randint(0, self.rozmiar), nrand.randint(0, self.rozmiar)]
            nazwa = nazwy[nrand.randint(0, len(nazwy))]
            # jesli pole nie jest zajete, dodajemy organizm
            if self.znajdz_organizm(polozenie, '') == None:
                if nazwa == 'Antylopa':
                    self.dodaj_organizm(Antylopa.Antylopa(polozenie, self))
                elif nazwa == 'Barszcz':
                    self.dodaj_organizm(Barszcz.Barszcz(polozenie, self))
                elif nazwa == 'Cyberowca':
                    self.dodaj_organizm(Cyberowca.Cyberowca(polozenie, self))
                elif nazwa == 'Guarana':
                    self.dodaj_organizm(Guarana.Guarana(polozenie, self))
                elif nazwa == 'Lis':
                    self.dodaj_organizm(Lis.Lis(polozenie, self))
                elif nazwa == 'Mlecz':
                    self.dodaj_organizm(Mlecz.Mlecz(polozenie, self))
                elif nazwa == 'Owca':
                    self.dodaj_organizm(Owca.Owca(polozenie, self))
                elif nazwa == 'Trawa':
                    self.dodaj_organizm(Trawa.Trawa(polozenie, self))
                elif nazwa == 'Wilcze jagody':
                    self.dodaj_organizm(WilczeJagody.WilczeJagody(polozenie, self))
                elif nazwa == 'Wilk':
                    self.dodaj_organizm(Wilk.Wilk(polozenie, self))
                elif nazwa == 'Zolw':
                    self.dodaj_organizm(Zolw.Zolw(polozenie, self))

    def rysuj_siatke(self, w, rows, surface):
        d = 25

        x = -d
        y = -d
        for l in range(rows+1):
            x = x + d
            y = y + d

            pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, w))
            pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))

    def get_organizmy(self):
        return self.organizmy

    def get_rozmiar(self):
        return self.rozmiar

    def get_okno(self):
        return self.okno

    def rysuj_swiat(self):
        self.okno.fill((255, 255, 255))  # Fills the screen with black
        self.rysuj_siatke(self.rozmiar*25, self.rozmiar, self.okno)  # Will draw our grid lines
        for organizm in self.organizmy:
            organizm.rysowanie()
        pygame.display.update()  # Updates the screen

    def dodaj_organizm(self, organizm):
        czy_dodany = False
        for i in range(len(self.organizmy)):
            if organizm.get_ini() > self.organizmy[i].get_ini():
                self.organizmy.insert(i, organizm)
                czy_dodany = True
                break
        if czy_dodany == False:
            self.organizmy.append(organizm)
        print(f'Dodano {organizm.get_gatunek()}')

    def znajdz_organizm(self, polozenie, nieorganizm):
        for organizm in self.organizmy:
            if polozenie == organizm.get_polozenie() and organizm != nieorganizm:
                return organizm
        return None

    def usun_organizm(self, organizm):
        self.organizmy.remove(organizm)

    def sprawdz_granice(self, polozenie):
        if polozenie[0] < 0 or polozenie[0] >= self.rozmiar or polozenie[1] < 0 or polozenie[1] >= self.rozmiar:
            return False
        else:
            return True

    def walka(self, organizm1, organizm2):
        index1 = self.organizmy.index(organizm1)
        index2 = self.organizmy.index(organizm2)
        if organizm1.get_sila() > organizm2.get_sila():
            self.usun_organizm(organizm2)
        elif organizm1.get_sila() < organizm2.get_sila():
            self.usun_organizm(organizm1)
        elif organizm1.get_sila() == organizm2.get_sila():
            if index1 > index2:
                self.usun_organizm(organizm1)
            else:
                self.usun_organizm(organizm2)

    def wykonaj_ture(self):
        for organizm in self.organizmy:
            self.rysuj_swiat()
            organizm.akcja()
            sleep(0.1)

    def wystartuj(self):
        tura = 0
        while True:
            tura += 1
            print(f'----- TURA {tura} -----')
            print('Organizmy:', [organizm.get_gatunek() for organizm in self.organizmy])
            self.wykonaj_ture()

    def wczytaj_stan(self):
        for organizm in self.organizmy:
            self.usun_organizm(organizm)

        plik = open('zapis.txt', 'r')
        linie = plik.readlines()
        rozmiar = int(linie[0].split(' ')[0])
        self.rozmiar = rozmiar

        for linia in linie[1:]:
            linia = linia.split(' ')
            polozenie = [int(linia[1]), int(linia[2])]
            if linia[0] == 'Czlowiek':
                self.dodaj_organizm(Czlowiek.Czlowiek(polozenie, self))
            elif linia[0] == 'Antylopa':
                self.dodaj_organizm(Antylopa.Antylopa(polozenie, self))
            elif linia[0] == 'Barszcz':
                self.dodaj_organizm(Barszcz.Barszcz(polozenie, self))
            elif linia[0] == 'Cyberowca':
                self.dodaj_organizm(Cyberowca.Cyberowca(polozenie, self))
            elif linia[0] == 'Guarana':
                self.dodaj_organizm(Guarana.Guarana(polozenie, self))
            elif linia[0] == 'Lis':
                self.dodaj_organizm(Lis.Lis(polozenie, self))
            elif linia[0] == 'Mlecz':
                self.dodaj_organizm(Mlecz.Mlecz(polozenie, self))
            elif linia[0] == 'Owca':
                self.dodaj_organizm(Owca.Owca(polozenie, self))
            elif linia[0] == 'Trawa':
                self.dodaj_organizm(Trawa.Trawa(polozenie, self))
            elif linia[0] == 'Wilcze jagody':
                self.dodaj_organizm(WilczeJagody.WilczeJagody(polozenie, self))
            elif linia[0] == 'Wilk':
                self.dodaj_organizm(Wilk.Wilk(polozenie, self))
            elif linia[0] == 'Zolw':
                self.dodaj_organizm(Zolw.Zolw(polozenie, self))

    def dodaj_po_gatunku(self, polozenie, gatunek):
        if gatunek == 'Antylopa':
            self.dodaj_organizm(Antylopa.Antylopa(polozenie, self))
        elif gatunek == 'Cyberowca':
            self.dodaj_organizm(Cyberowca.Cyberowca(polozenie, self))
        elif gatunek == 'Lis':
            self.dodaj_organizm(Lis.Lis(polozenie, self))
        elif gatunek == 'Owca':
            self.dodaj_organizm(Owca.Owca(polozenie, self))
        elif gatunek == 'Wilk':
            self.dodaj_organizm(Wilk.Wilk(polozenie, self))
        elif gatunek == 'Zolw':
            self.dodaj_organizm(Zolw.Zolw(polozenie, self))

