from Organizm import Organizm
import Swiat
import numpy.random as nrand
import pygame


class Roslina(Organizm):

    def kolizja(self, organizm):
        return False

    def get_ini(self):
        return self.ini

    def get_polozenie(self):
        return self.polozenie

    def get_sila(self):
        return self.sila

    def get_gatunek(self):
        return self.gatunek

    def rysowanie(self):
        d = 25
        i = self.polozenie[0]
        j = self.polozenie[1]

        pygame.draw.rect(self.swiat.get_okno(), self.kolor, (i*d+1,j*d+1, d-1, d-1))