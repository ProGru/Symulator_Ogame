from Statek import Statek


class Flota():

    def __init__(self, file_name):
        self.ship_list = self.zaladuj_flote(file_name)


    def zaladuj_flote(self,file_name):
        """
        :param file_name: file where flota is
        :return: ship list with all ships from
        """
        wszystko_z_pliku = open(file_name).readlines()[1:]
        statki_w_flocie = []
        ship_list =[]

        for i in wszystko_z_pliku:
            statki_w_flocie.append(i.rsplit())

        for i in statki_w_flocie:
            for j in range(0,int(i[1])):
                ship_list.append(Statek(i[0]))

        return ship_list

    def __str__(self):
        return str(self.ship_list)

