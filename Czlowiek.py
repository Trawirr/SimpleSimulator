from Zwierze import Zwierze
import pygame

class Czlowiek(Zwierze):
    def __init__(self, polozenie, swiat):
        self.sila = 5
        self.ini = 5
        self.polozenie = polozenie
        self.swiat = swiat
        self.kolor = (55, 135, 225)
        self.gatunek = "Czlowiek"
        self.tarcza = False
        self.odnowienie = 0
        print(f"{self.gatunek} {self.polozenie} stworzony")

    def akcja(self):
        self.odnowienie -= 1
        if self.odnowienie < 6:
            self.tarcza = False
        print(self.get_gatunek(), self.get_polozenie(), "przemieszcza się na", end=' ')
        walka = False
        wczytanie = False
        ruch = [0, 0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Wyjscie")
                pygame.quit()

            event = pygame.event.wait()
            keys = pygame.key.get_pressed() # czytanie nacisnietego klawisza
            for key in keys:
                if keys[pygame.K_LEFT]:
                    ruch = [-1, 0]

                elif keys[pygame.K_RIGHT]:
                    ruch = [1, 0]

                elif keys[pygame.K_UP]:
                    ruch = [0, -1]

                elif keys[pygame.K_DOWN]:
                    ruch = [0, 1]

                #uzycie umiejetnosci
                elif keys[pygame.K_RETURN]:
                    if self.odnowienie <= 0:
                        self.tarcza = True
                        self.odnowienie = 10

                # wyjscie i zapis stanu
                elif keys[pygame.K_ESCAPE]:
                    plik = open('zapis.txt', 'w')
                    plik.write(f'{self.swiat.get_rozmiar()} \n')
                    for organizm in self.swiat.get_organizmy():
                        plik.write(f'{organizm.get_gatunek()} {organizm.get_polozenie()[0]} {organizm.get_polozenie()[1]} \n')
                    pygame.quit()

                # wczytanie stanu
                elif keys[pygame.K_l]:
                    wczytanie = True

        if wczytanie == True:
            self.swiat.wczytaj_stan()
            return 0

        # jesli pole miesci sie w wymiarach swiata i organizm na tym polu nie uniemozliwil ruchu
        if self.swiat.sprawdz_granice([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]]):
            kolidujacy = self.swiat.znajdz_organizm([self.polozenie[0] + ruch[0], self.polozenie[1] + ruch[1]], self)
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
        if self.tarcza == True:
            return True
        else:
            return False