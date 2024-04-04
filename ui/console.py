from service.evenimenteService import EvenimenteService
from service.persoanaServiceReports import ReportsService
from service.persoaneService import PersoaneService


class Consola:
    def __init__(self, persoaneService: PersoaneService, evenimenteService: EvenimenteService, rapoarteService: ReportsService):
        # in console se va crea un nou PersoaneService
        # in console se va crea un nou EvenimenteService
        self.__PersoaneService = persoaneService
        self.__EvenimenteService = evenimenteService
        self.__RapoarteService = rapoarteService

    def adaugaPers(self):
        try:
            # in functie se vor citi de la tastatura datele persoanelor si evenimentelor
            optt = input("1. persoana --> 2. eveniment: ")
            if optt == "1":
                idP = input("Dati id-ul persoanei: ")
                nume = input("Dati numele persoanei: ")
                adresa = input("Dati adresa persoanei: ")
                listp = []
                self.__PersoaneService.adauga(idP, nume, adresa, listp)
            elif optt == "2":
                idE = input("Dati id-ul evenimentului: ")
                data = input("Dati data evenimentului: ")
                timp = input("Dati durata evenimentului: ")
                desc = input("Dati descrierea evenimentului: ")
                cnt = 0
                self.__EvenimenteService.adauga(idE, data, timp, desc, cnt)
        except KeyError as e:
            print(e)

    def modificaPers(self):
        try:
            # in functie se vor citi date noi de la tastura pentru persoane sau evenimente
            optt = input("1. persoana --> 2. eveniment: ")
            if optt == "1":
                idP = input("Dati id-ul persoanei de modificat: ")
                numeN = input("Dati numele nou al persoanei: ")
                adresaN = input("Dati noua adresa a persoanei: ")
                listN = []
                list_l = int(input("Introduceti lungimea listei de inscrieri: "))
                i = 0
                while i < list_l:
                    e_id = input("Introduceti id-ul evenimentului de adaugat: ")
                    listN.append(e_id)
                    i += 1
                self.__PersoaneService.modifica(idP, numeN, adresaN, listN)
            elif optt == "2":
                idE = input("Dati id-ul evenimentului de modificat: ")
                dataN = input("Dati data noua al persoanei: ")
                timpN = input("Dati noua durata a persoanei: ")
                descN = input("Dati noua descriere a evenimentului: ")
                cntN = int(input("Dati noua inscriere la eveniment: "))
                self.__EvenimenteService.modifica(idE, dataN, timpN, descN, cntN)
        except KeyError as e:
            print(e)

    def sterge(self):
        try:
            # in functie se citeste id-ul persoanei sau al evenimentului care ulterior va fi sters
            optt = input("1. persoana --> 2. eveniment: ")
            if optt == "1":
                idP = input("Dati id-ul persoanei de sters: ")
                self.__PersoaneService.sterge(idP)
            elif optt == "2":
                idE = input("Dati id-ul evenimentului de sters: ")
                self.__EvenimenteService.sterge(idE)
        except KeyError as e:
            print(e)

    def findby(self):
        optt = input("1. persoana --> 2.eveniment: ")
        if optt == "1":
            try:
                idP = input("Dati id-ul persoanei de cautat: ")
                k = self.__PersoaneService.findByid(idP)
                if k is None:
                    raise KeyError("Nu exista persoana cu id-ul dat! ")
                print(k)
            except KeyError as e:
                print(e)
        elif optt == "2":
            try:
                idE = input("Dati id-ul evenimentului de cautat: ")
                k = self.__EvenimenteService.findByid(idE)
                if k is None:
                    raise KeyError("Nu exista persoana cu id-ul dat! ")
            except KeyError as er:
                print(er)

    def signE(self):
        try:
            # in  functie se citeste id-ul evenimentului si al persoanei care se inscrie
            self.afiseaza(self.__EvenimenteService.getALLe())
            ides = input("Introduceti id-ul evenimentului: ")
            self.__EvenimenteService.signEvenid(ides)
            self.afiseaza(self.__PersoaneService.getALLp())
            idps = input("Introduceti id-ul persoanei:")
            self.__PersoaneService.sign(ides, idps)
        except KeyError as e:
            print(e)

    def signES(self):
        try:
            # functia returneaza si afiseaza lista de evenimente sortata dupa
            self.afiseaza(self.__EvenimenteService.signEvenS())

        except KeyError as e:
            print(e)

    def signESm(self):
        try:
            # functia returneaza si afiseaza lista de persoane cu cele mai multe evenimente
            self.afiseaza(self.__PersoaneService.ordM())
            print("-----------------------------------------")
            self.afiseaza(self.__RapoarteService.ordM())
        except KeyError as e:
            print(e)

    def twppp(self):
        try:
            # functia afiseaza o lista cu primele 20% evenimente cu cei mai multi invitati
            self.printtwp(self.__EvenimenteService.twp())
            print("------------------------------------------")
            self.afiseaza(self.__RapoarteService.twp())
        except KeyError as e:
            print(e)

    def printtwp(self, listtwp):
        for i in listtwp:
            print(f"descriere: {i.getdesc()} nr. participanti: {i.getcnt()}")

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    @staticmethod
    def printMeniu():
        print("1. Adauga.")
        print("2. Modifica.")
        print("3. Sterge.")
        print("4. Cauta.")
        print("5. Inscriere.")
        print("6. Sortare.")
        print("7. Lista de persoane inscrise la cele mai multe evenimente.")
        print("8. 20%")
        print("all. Afiseaza.")
        print("x. Iesire")

    def meniu(self):
        self.printMeniu()
        while True:
            opt = input("Dati optiunea: ")
            if opt == "1":
                self.adaugaPers()
            elif opt == "2":
                self.modificaPers()
            elif opt == "3":
                self.sterge()
            elif opt == "4":
                self.findby()
            elif opt == "5":
                self.signE()
            elif opt == "6":
                self.signES()
            elif opt == "7":
                self.signESm()
            elif opt == "8":
                self.twppp()
            elif opt == "all":
                k = input("1. persoane --> 2. evenimente: ")
                if k == "1":
                    self.afiseaza(self.__PersoaneService.getALLp())
                elif k == "2":
                    self.afiseaza(self.__EvenimenteService.getALLe())
            elif opt == "x":
                break
            else:
                print("Optiune gresita, reincercati! ")
