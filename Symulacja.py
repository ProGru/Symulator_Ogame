from Flota import Flota
import random
import time

class Symulacja():

    def __init__(self):
        self.flota1 = Flota()
        self.flota2 = Flota()

    def zaladuj_floty_lista(self,lista1,lista2):
        self.flota1.zaladuj_flote_lista(lista1)
        self.flota2.zaladuj_flote_lista(lista2)

    def zaladuj_floty_plik(self,file1,file2):
        self.flota1.zaladuj_flote_plik(file1)
        self.flota2.zaladuj_flote_plik(file2)

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
            self.flota1.reset()
            self.flota2.reset()
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
                wybrany = random.choice(self.flota2.ship_list)
                wybrany.do_atack(i)
                while wybrany.can_shot_more(i):
                    wybrany = random.choice(self.flota2.ship_list)
                    wybrany.do_atack(i)

        for i in self.flota2:
            if len(self.flota1)>0:
                wybrany = random.choice(self.flota1.ship_list)
                wybrany.do_atack(i)
                while wybrany.can_shot_more(i):
                    wybrany = random.choice(self.flota2.ship_list)
                    wybrany.do_atack(i)




        niezniszczona_flota1 = []
        niezniszczona_flota2 = []

        for i in self.flota1:
            if i.is_live():
                i.odnow_oslone()
                niezniszczona_flota1.append(i)
        self.flota1.ship_list = niezniszczona_flota1

        for i in self.flota2:
            if i.is_live():
                i.odnow_oslone()
                niezniszczona_flota2.append(i)
        self.flota2.ship_list = niezniszczona_flota2



"""
symulacja = Symulacja()
#symulacja.zaladuj_floty_plik("flota1","flota2")
symulacja.zaladuj_floty_lista([("mt", 120000),("ow",10)],[("ow",1000)])
przed = time.time()
print symulacja.usredniony_wynik_symulacji(1)
po = time.time()

print po-przed

print len(symulacja.flota1)
print len(symulacja.flota2)
"""