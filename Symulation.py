from Flota import Flota
import random

class Symulation():

    def __init__(self):
        self.flota1 = Flota()
        self.flota2 = Flota()

    def load_flota_from_list(self, list1, list2):
        self.flota1.load_flota_list(list1)
        self.flota2.load_flota_list(list2)

    def load_flota_from_file(self, file1, file2):
        self.flota1.load_flota_file(file1)
        self.flota2.load_flota_file(file2)

    def do_symulation(self, rounds):
        """
        wykonuje symulacje calej bitwy o podanej ilosci rund
        :param rounds: ilosc rund w bitwie
        :return: True - wygrala flota 1, False - wyglala flota 2, None - remis
        """

        for i in range(0, rounds):
            self.fight()

        if len(self.flota1)>0 and len(self.flota2)>0 or len(self.flota1)==0 and len(self.flota2) ==0:
            return None
        elif len(self.flota1)>0:
            return True
        else:
            return False

    def averaged_results_symulation(self, how_much_symulations):
        """
        Wykonuje podana ilosc symulacji i wybiera najwieksza ilosc wystapien wyniku
        :param how_much_symulations: ile symulacji ma wykonac program
        :return: zwraca ktora flota wygrala badz remis
        """
        flota1 = 0
        flota2 = 0
        remis = 0

        for i in range(0, how_much_symulations):
            self.flota1.reset()
            self.flota2.reset()
            result = self.do_symulation(6)
            if result:
                flota1 += 1
            elif result == None:
                remis += 1
            else:
                flota2 += 1
        if flota1>flota2 and flota1>remis:
            return "flota1"
        elif flota1==flota2 or flota2<remis:
            return "remis"
        else:
            return "flota2"

    def fight(self):
        """
        symulacja pojedynczej rundy w bitwie.
        zmienia jedynie sytuacje w obiektach statek
        """

        for i in self.flota1:
            if len(self.flota2)>0:
                chosen = random.choice(self.flota2.ship_list)
                chosen.do_atack(i)
                while chosen.can_shot_more(i):
                    chosen = random.choice(self.flota2.ship_list)
                    chosen.do_atack(i)

        for i in self.flota2:
            if len(self.flota1)>0:
                chosen = random.choice(self.flota1.ship_list)
                chosen.do_atack(i)
                while chosen.can_shot_more(i):
                    chosen = random.choice(self.flota2.ship_list)
                    chosen.do_atack(i)




        not_destroyed_flot1 = []
        not_destroyed_flot2 = []

        for i in self.flota1:
            if i.is_live():
                i.shield_regeneration()
                not_destroyed_flot1.append(i)
        self.flota1.ship_list = not_destroyed_flot1

        for i in self.flota2:
            if i.is_live():
                i.shield_regeneration()
                not_destroyed_flot2.append(i)
        self.flota2.ship_list = not_destroyed_flot2
