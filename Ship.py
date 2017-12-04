import Ships_data
import random

class Ship():

    def __init__(self, ship_short):
        self.ship_parameters = Ships_data.ship_type
        self.fast_cannon = Ships_data.fast_cannon

        self.ship_short = ship_short

        self.ship_name, self.structurals_points, self.shield, self.atack = self.get_info_ship(ship_short)
        self.live = True


    def get_info_ship(self, short_ship):
        """
        looking for name and return all stats of ship
        :param short_ship:
        :return all stats of ship:
        """
        for i in self.ship_parameters:
            if i[0] == short_ship:
                return i[1][:], int(i[2][:]), int(i[3][:]), int(i[4][:])

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
            self.structurals_points = 0
            self.live = False

        if self.structurals_points <= 0:
            self.live = False




    def add_damage(self,ship):
        """
        add damage to self ship
        :param ship : atacking ship
        """
        if self.shield*0.01 < ship.atack:
            if self.shield > 0:
                self.shield -= ship.atack
            else:
                self.structurals_points -= ship.atack

            if self.shield < 0:
                self.structurals_points += self.shield
                self.shield = 0

    def can_shot_more(self,ship):
        """
        check that ship can shot twice time
        :param ship:
        :return True or False:
        """
        chance = 1 - (1.0 / self.find_fast_cannon(ship))
        if chance > 0:
            chance_shot = random.uniform(0, 1)
            return chance >= chance_shot
        else:
            return False


    def will_burn(self):
        """
        check that ship have to much damage
        :return True or False:
        """

        if self.structurals_points < self.get_info_ship(self.ship_short)[1] * 0.7:
            chance_explosion = 1.0 - (float(self.structurals_points) / self.get_info_ship(self.ship_short)[1])
            chance = random.uniform(0, 1)
            return chance<chance_explosion
        else:
            return False

    def is_live(self):
        """
        check that ship is live or destroy
        :return True or False :
        """
        return self.live

    def find_fast_cannon(self, ship):
        """
        find value of fast_cannon for two ship
        :param ship: atacking ship
        :return value of fast_cannon:
        """
        intex1 = 0
        index2 = 0

        for i in range(0, len(self.fast_cannon[0])):
            if self.fast_cannon[0][i] == self.ship_short:
                index1 = i
            if self.fast_cannon[0][i] == ship.ship_short:
                index2 = i
        return int(self.fast_cannon[index1][index2])

    def shield_regeneration(self):
        """
        if ship live restore shields to max value
        """
        if self.is_live():
            self.shield = self.get_info_ship(self.ship_short)[2]

    def __str__(self):
        return "nazwa: " + self.ship_short + " oslona:" + str(self.shield) + " zycie:" + str(self.structurals_points) + " zyje:" + str(self.is_live())

