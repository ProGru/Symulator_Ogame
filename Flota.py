from Statek import Statek


class Flota():

    def __init__(self,file_name):
        self.file_name = file_name
        self.ship_list = self.zaladuj_flote(file_name)


    def zaladuj_flote(self,file_name):
        wszystko_z_pliku = open(file_name).readlines()[1:]
        statki_w_flocie = []
        ship_list =[]

        for i in wszystko_z_pliku:
            statki_w_flocie.append(i.rsplit())

        for i in statki_w_flocie:
            statki_typu = []
            for j in range(0,int(i[1])):
                statki_typu.append(Statek(i[0]))
            ship_list.append(statki_typu)

        return ship_list

    def __str__(self):
        return str(self.ship_list)
