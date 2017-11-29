from Statek import Statek


class Flota():

    def __init__(self):
        self.ship_list = []
        self.zapasowa_lista = []


    def zaladuj_flote_plik(self, file_name):
        """
        :param file_name: file where flota is
        :return: ship list with all ships from
        """
        wszystko_z_pliku = open(file_name).readlines()
        statki_w_flocie = []
        ship_list =[]

        for i in wszystko_z_pliku:
            statki_w_flocie.append(i.rsplit())

        for i in statki_w_flocie:
            for j in range(0,int(i[1])):
                ship_list.append(Statek(i[0]))

        self.ship_list = ship_list
        self.zapasowa_lista = ship_list

    def zaladuj_flote_lista(self, data):
        """
        przypisuje statki do floty
        :param data: lista statkow do stworzenia np [("mt",100),("dt",1)]
        :return: zwraca liste obiektow klasy Statek
        """
        ship_list =[]

        for i in data:
            for j in range(0,i[1]):
                ship_list.append(Statek(i[0]))

        self.ship_list =  ship_list
        self.zapasowa_lista = ship_list

    def reset(self):
        self.ship_list = self.zapasowa_lista


    def __str__(self):
        return str(self.ship_list)

    def __len__(self):
        return len(self.ship_list)

    def __iter__(self):
        for i in range(0,len(self.ship_list)):
            yield self.ship_list[i]

    def __setitem__(self, key, value):
        self.ship_list = value


