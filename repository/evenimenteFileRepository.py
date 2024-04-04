from domain.evenimente import Evenimente
from repository.evenimenteRepository import EvenimenteRepository


class EvenimenteFileRepository(EvenimenteRepository):
    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_dinf()

    def adaugae(self, eveniment):
        super().adaugae(eveniment)
        self.scrie_inf()

    def modificae(self, eveniment):
        super().modificae(eveniment)
        self.scrie_inf()

    def sterge(self, eveniment):
        super().sterge(eveniment)
        self.scrie_inf()

    def citeste_dinf(self):
        try:
            f = open(self.__nume_fisier, "r")
            linie = f.readline().strip("\n")
            while linie != "":
                lista_atr = linie.split(",")
                idE = lista_atr[0]
                data = lista_atr[1]
                timp = lista_atr[2]
                desc = lista_atr[3]
                cnt = lista_atr[4]
                eveniment = Evenimente(idE, data, timp, desc, cnt)
                super().adaugae(eveniment)
                linie = f.readline().strip("\n")
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului! " + self.__nume_fisier)

    def scrie_inf(self):
        try:
            f = open(self.__nume_fisier, "w")
            list_e = super().getALL()
            for even in list_e:
                idE = even.getidE()
                data = even.getdata()
                timp = even.gettimp()
                desc = even.getdesc()
                cnt = even.getcnt()
                linie = idE + "," + data + "," + timp + "," + desc + "," + str(cnt) + "\n"
                f.write(linie)
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului! " + self.__nume_fisier)
