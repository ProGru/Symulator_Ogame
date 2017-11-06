from Flota import Flota
import random
import time

class Symulacja():

    def __init__(self,flota1,flota2):
        self.file1 = flota1
        self.file2 = flota2
        self.flota1 = Flota(flota1).zaladuj_flote(flota1)
        self.flota2 = Flota(flota2).zaladuj_flote(flota2)

    def wykonaj_symulacje(self, rundy):
        """
        wykonuje symulacje calej bitwy o podanej ilosci rund
        :param rundy: ilosc rund w bitwie
        :return: True - wygrala flota 1, False - wyglala flota 2, None - remis
        """

        for i in range(0,rundy):
            wynik = self.bitwa()

        if len(self.flota1)>0 and len(self.flota2)>0 or len(self.flota1)==0 and len(self.flota2) ==0:
            return None
        elif len(self.flota1)>0:
            return True
        else:
            return False

    def usredniony_wynik_symulacji(self,ile_symulacji):
        """
        Wykonuje podana ilosc symulacji i wybiera najwieksza ilosc wystapien wyniku
        :param ile_symulacji: ile symulacji ma wykonac program
        :return: zwraca ktora flota wygrala badz remis
        """
        flota1 = 0
        flota2 = 0
        remis = 0

        for i in range(0,ile_symulacji):
            self.__init__(self.file1,self.file2)
            wynik = self.wykonaj_symulacje(6)
            if wynik:
                flota1 += 1
            elif wynik == None:
                remis += 1
            else:
                flota2 += 1
        if flota1>flota2 and flota1>remis:
            return "flota1"
        elif flota1==flota2 or flota2<remis:
            return "remis"
        else:
            return "flota2"

    def bitwa(self):
        """
        symulacja pojedynczej rundy w bitwie.
        zmienia jedynie sytuacje w obiektach statek
        """

        for i in self.flota1:
            if len(self.flota2)>0:
                wybrany = random.choice(self.flota2)
                wybrany.do_atack(i)

        for i in self.flota2:
            if len(self.flota1) >0:
                wybrany = random.choice(self.flota1)
                wybrany.do_atack(i)

        niezniszczona_flota1 = []
        niezniszczona_flota2 = []

        for i in self.flota1:
            if i.is_live():
                i.odnow_oslone()
                niezniszczona_flota1.append(i)
        self.flota1 = niezniszczona_flota1

        for i in self.flota2:
            if i.is_live():
                i.odnow_oslone()
                niezniszczona_flota2.append(i)
        self.flota2 = niezniszczona_flota2




symulacja = Symulacja("flota1","flota2")

przed = time.time()
print symulacja.usredniony_wynik_symulacji(100)
po = time.time()

print po-przed