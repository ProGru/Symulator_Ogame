import Parametry_statkow

class Statek():

    def __init__(self, nazwa_statku):
        self.parametry_statkow = Parametry_statkow.ship_type
        self.szybkie_dziala = Parametry_statkow.szybkie_dziala

        self.nazwa_statku = nazwa_statku

        self.skrot_statku, self.punkty_strukturalne, self.oslona, self.atak = self.get_info_ship(nazwa_statku)
        self.live = True


    def get_info_ship(self, nazwa_statku):
        for i in self.parametry_statkow:
            if i[1] == nazwa_statku:
                return i[0],int(i[2]),int(i[3]),int(i[4])

    def add_damage(self,damage):
        if self.oslona > 0:
            self.oslona -= damage
        else:
            self.punkty_strukturalne -= damage

        if self.oslona < 0:
            self.punkty_strukturalne += self.oslona
            self.oslona = 0

        if self.punkty_strukturalne <= 0:
            self.live = False


new = Statek("du\xc5\xbcy_transporter")
print "before"
print new.oslona
print new.punkty_strukturalne
new.add_damage(1100)
print "after"
print new.oslona
print new.punkty_strukturalne
