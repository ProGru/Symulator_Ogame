class Ships_data():
    def __init__(self):
        return

    def get_ship_type(self):
        """
        open and read from fille list of params of ships
        :return: list of params
        """
        everything_from_file = open('dane_statkow').readlines()[1:]
        all_ship = []
        for i in everything_from_file:
            all_ship.append(i.rsplit())
        return all_ship

    def get_fast_cannon(self):
        """
        open and read from fille list of fast_cannon table
        :return: fast_canon Array
        """
        everything_from_file = open('szybkie_dziala').readlines()
        cannon_data = []
        for i in everything_from_file:
            cannon_data.append(i.rsplit())
        return cannon_data

data = Ships_data()
ship_type = data.get_ship_type()
fast_cannon = data.get_fast_cannon()
