from appJar import gui
import Ships_data
import Symulation

class Play():
    def __init__(self, app):
        self.app = app

    def __call__(self, *args, **kwargs):
        symulation = Symulation.Symulation()
        apply_result = Apply(self.app).__call__()

        symulation.load_flota_from_list(apply_result[0], apply_result[1])
        app.infoBox("wynik", symulation.averaged_results_symulation(1))


class Apply():
    def __init__(self, app):
        self.app = app


    def __call__(self, *args, **kwargs):
        lista = []
        for i in Ships_data.ship_type:
            lista.append(i[0])

        flota1 = []
        flota2 = []

        for i in lista:
            if self.app.getEntry(i + '1') != '':
                flota1.append((i, int(self.app.getEntry(i + "1"))))
            else:
                flota1.append((i, 0))

            if self.app.getEntry(i+'2') != '':
                flota2.append((i, int(self.app.getEntry(i + "2"))))
            else:
                flota2.append((i, 0))
        return flota1, flota2
kolumna1 = 0
kolumna2 = 1
wiersz = 0
app = gui("OGAME")
app.addLabel("label1", "Flota 1", wiersz, kolumna1)
app.addLabelEntry("mt1", wiersz + 1, kolumna1)
app.addLabelEntry("dt1", wiersz + 2, kolumna1)
app.addLabelEntry("lm1", wiersz + 3, kolumna1)
app.addLabelEntry("cm1", wiersz + 4, kolumna1)
app.addLabelEntry("kr1", wiersz + 5, kolumna1)
app.addLabelEntry("ow1", wiersz + 6, kolumna1)
app.addLabelEntry("sk1", wiersz + 7, kolumna1)
app.addLabelEntry("re1", wiersz + 8, kolumna1)
app.addLabelEntry("ss1", wiersz + 9, kolumna1)
app.addLabelEntry("b1", wiersz + 10, kolumna1)
app.addLabelEntry("n1", wiersz + 11, kolumna1)
app.addLabelEntry("gs1", wiersz + 12, kolumna1)
app.addLabelEntry("p1", wiersz + 13, kolumna1)

app.addLabel("label2", "Flota 2", wiersz, kolumna2)

app.addLabelEntry("mt2", wiersz + 1, kolumna2)
app.addLabelEntry("dt2", wiersz + 2, kolumna2)
app.addLabelEntry("lm2", wiersz + 3, kolumna2)
app.addLabelEntry("cm2", wiersz + 4, kolumna2)
app.addLabelEntry("kr2", wiersz + 5, kolumna2)
app.addLabelEntry("ow2", wiersz + 6, kolumna2)
app.addLabelEntry("sk2", wiersz + 7, kolumna2)
app.addLabelEntry("re2", wiersz + 8, kolumna2)
app.addLabelEntry("ss2", wiersz + 9, kolumna2)
app.addLabelEntry("b2", wiersz + 10, kolumna2)
app.addLabelEntry("n2", wiersz + 11, kolumna2)
app.addLabelEntry("gs2", wiersz + 12, kolumna2)
app.addLabelEntry("p2", wiersz + 13, kolumna2)
app.addButtons(["apply", "play"], [Apply(app), Play(app)], wiersz + 14, kolumna1)


app.go()