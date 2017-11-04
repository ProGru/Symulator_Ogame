from Flota import Flota


class Symulacja():

    def __init__(self,flota1,flota2):
        self.flota1 = Flota(flota1)
        self.flota2 = Flota(flota2)

    def wykonaj_symulacje(self):
        print self.flota1
        print self.flota2


symulacja = Symulacja("flota1","flota2")

symulacja.wykonaj_symulacje()