import Parametry_statkow
import random

class Statek():

    def __init__(self, skrot_statku):
        self.parametry_statkow = Parametry_statkow.ship_type
        self.szybkie_dziala = Parametry_statkow.szybkie_dziala

        self.skrot_statku = skrot_statku

        self.nazwa_statku, self.punkty_strukturalne, self.oslona, self.atak = self.get_info_ship(skrot_statku)
        self.live = True


    def get_info_ship(self, skrot_statku):
        """
        looking for name and return all stats of ship
        :param skrot_statku:
        :return all stats of ship:
        """
        for i in self.parametry_statkow:
            if i[0] == skrot_statku:
                return i[1][:],int(i[2][:]),int(i[3][:]),int(i[4][:])

    def do_atack(self,ship):
        """
        :param ship: atacking ship
        function implements atack ship on this ship
        first add damage then
        check that ship can shot again and if it is posible do it
        check that ship can burn and if destroy ship
        """
        self.add_damage(ship)


        #if self.can_shot_more(ship):
            #self.add_damage(ship)

        if self.will_burn():
            self.punkty_strukturalne = 0
            self.live = False

        if self.punkty_strukturalne <= 0:
            self.live = False




    def add_damage(self,ship):
        """
        add damage to self ship
        :param ship : atacking ship
        """
        if self.oslona*0.01 < ship.atak:
            if self.oslona > 0:
                self.oslona -= ship.atak
            else:
                self.punkty_strukturalne -= ship.atak

            if self.oslona < 0:
                self.punkty_strukturalne += self.oslona
                self.oslona = 0

    def can_shot_more(self,ship):
        """
        check that ship can shot twice time
        :param ship:
        :return True or False:
        """
        chance = 1 - (1.0/self.find_szybkie_dzialo(ship))
        print chance
        if chance>0:
            chance_shot = random.uniform(0,1)
            return chance >= chance_shot
        else:
            return False


    def will_burn(self):
        """
        check that ship have to much damage
        :return True or False:
        """

        if self.punkty_strukturalne < self.get_info_ship(self.skrot_statku)[1] * 0.7:
            chance_explosion = 1.0 - (float(self.punkty_strukturalne) / self.get_info_ship(self.skrot_statku)[1])
            chance = random.uniform(0,1)
            return chance<chance_explosion
        else:
            return False

    def is_live(self):
        """
        check that ship is live or destroy
        :return True or False :
        """
        return self.live

    def find_szybkie_dzialo(self, ship):
        """
        find value of szybkie_dzialo for two ship
        :param ship: atacking ship
        :return value of szybkie_dzialo:
        """
        intex1 = 0
        index2 = 0

        for i in range(0,len(self.szybkie_dziala[0])):
            if self.szybkie_dziala[0][i] == self.skrot_statku:
                index1 = i
            if self.szybkie_dziala[0][i] == ship.skrot_statku:
                index2 = i
        return int(self.szybkie_dziala[index1][index2])

    def odnow_oslone(self):
        """
        if ship live restore oslona to max value
        """
        if self.is_live():
            self.oslona = self.get_info_ship(self.skrot_statku)[2]

    def __str__(self):
        return "nazwa: " + self.skrot_statku +" oslona:" + str(self.oslona) + " zycie:" + str(self.punkty_strukturalne) + " zyje:" + str(self.is_live())

