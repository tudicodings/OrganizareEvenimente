from domain.persoane import Persoane
from repository.persoaneRepository import PersoaneRepository


class PersoaneFileRepository(PersoaneRepository):
    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_dinf()

    def adauga(self, persoana):
        super().adauga(persoana)
        self.scrie_inf()

    def modifica(self, persoana):
        super().modifica(persoana)
        self.scrie_inf()

    def sterge(self, persoana):
        super().sterge(persoana)
        self.scrie_inf()

    def citeste_dinf(self):
        try:
            f = open(self.__nume_fisier, "r")
            linie = f.readline().strip("\n")
            while linie != "":
                lista_atr = linie.split(",")
                idP = lista_atr[0]
                nume = lista_atr[1]
                adresa = lista_atr[2]
                list_even = []
                persoana = Persoane(idP, nume, adresa, list_even)
                super().adauga(persoana)
                linie = f.readline().strip("\n")
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului! " + self.__nume_fisier)

    def scrie_inf(self):
        try:
            f = open(self.__nume_fisier, "w")
            list_p = super().getALL()
            for pers in list_p:
                idP = pers.getidP()
                nume = pers.getnume()
                adresa = pers.getadresa()
                list_even = pers.getlisteven()
                linie = idP + "," + nume + "," + adresa + "," + str(list_even) + "\n"
                f.write(linie)
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului! " + self.__nume_fisier)
