class Dane_statkow():
    def __init__(self):
        return

    def get_ship_type(self):
        wszystko_z_pliku = open('dane_statkow').readlines()[1:]
        wszystkie_statki = []
        for i in wszystko_z_pliku:
            wszystkie_statki.append(i.rsplit())
        return wszystkie_statki

    def get_szybkie_dziala(self):
        wszystko_z_pliku = open('szybkie_dziala').readlines()
        dane_dzial = []
        for i in wszystko_z_pliku:
            dane_dzial.append(i.rsplit())
        return dane_dzial

dane = Dane_statkow()
ship_type = dane.get_ship_type()
szybkie_dziala = dane.get_szybkie_dziala()
