from Ship import Ship


class Flota():

    def __init__(self):
        self.ship_list = []
        self.backup_list = []


    def load_flota_file(self, file_name):
        """
        :param file_name: file where flota is
        :return: ship list with all ships from fille
        """
        everything_from_file = open(file_name).readlines()
        ships_in_flota = []
        ship_list =[]

        for i in everything_from_file:
            ships_in_flota.append(i.rsplit())

        for i in ships_in_flota:
            for j in range(0,int(i[1])):
                ship_list.append(Ship(i[0]))

        self.ship_list = ship_list
        self.backup_list = ship_list

    def load_flota_list(self, data):
        """
        create flota from ship list
        :param data: list ships to create for example [("mt",100),("dt",1)]
        :return: list with object class Ship
        """
        ship_list =[]

        for i in data:
            for j in range(0,i[1]):
                ship_list.append(Ship(i[0]))

        self.ship_list =  ship_list
        self.backup_list = ship_list

    def reset(self):
        """
        reset ship list for example when old one is changed
        """
        self.ship_list = self.backup_list


    def __str__(self):
        return str(self.ship_list)

    def __len__(self):
        return len(self.ship_list)

    def __iter__(self):
        for i in range(0,len(self.ship_list)):
            yield self.ship_list[i]

    def __setitem__(self, key, value):
        self.ship_list = value


