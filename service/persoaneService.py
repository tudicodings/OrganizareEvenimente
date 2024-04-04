from domain.persoane import Persoane


class PersoaneService:
    def __init__(self, persoaneRepository, evenimenteRepository):
        self.__PersoaneRepository = persoaneRepository
        self.__EvenimenteRepository = evenimenteRepository

    def getALLp(self):
        # returneaza o lista cu toate persoanele
        return self.__PersoaneRepository.getALL()

    def adauga(self, idpers, nume, adresa, lista):
        # adauga o noua persoana in dictionar daca nu exista deja, altfel KeyError
        persoana = Persoane(idpers, nume, adresa, lista)
        self.__PersoaneRepository.adauga(persoana)

    def modifica(self, idpers, numen, adresan, listn):
        # modifica o persoana in dictionar daca exsita, altfel KeyError
        persn = Persoane(idpers, numen, adresan, listn)
        self.__PersoaneRepository.modifica(persn)

    def sterge(self, idpers):
        # sterge o persoana dupa un id dat daca exista in dictionar, altfel KeyError
        self.__PersoaneRepository.sterge(idpers)

    def findByid(self, idpers):
        # in cazul in care exista o persoana cu id-ul dat o returneaza, altfel KeyError
        return self.__PersoaneRepository.getByid(idpers)

    def sign(self, ideven, idpers):
        # verifica daca exista eveniment in dictionar dupa ideven si adauga listei de evenimente
        # inregistrate id-ul evenimentului, altfel scade nr de inscrieri si KeyError
        if self.findByid(idpers) is None:
            even = self.__EvenimenteRepository.getByid(ideven)
            insc = even.getcnt()
            insc -= 1
            even.setcnt(insc)
            self.__EvenimenteRepository.modificae(even)
            raise KeyError("Nu exista persoana cu id-ul dat!")
        pers = self.__PersoaneRepository.getByid(idpers)
        listi = pers.getlisteven()
        listi.append(ideven)
        self.modifica(idpers, pers.getnume(), pers.getadresa(), listi)

    def ordM(self):
        listPr = self.getALLp()
        aux = Persoane("0", "0", "0", [])
        for i in range(0, len(listPr) - 1):
            for j in range(i+1, len(listPr)):
                if len(listPr[i].getlisteven()) < len(listPr[j].getlisteven()):
                    aux.setidP(listPr[i].getidP())
                    aux.setnume(listPr[i].getnume())
                    aux.setadresa(listPr[i].getadresa())
                    aux.setlisteven(listPr[i].getlisteven())

                    listPr[i].setidP(listPr[j].getidP())
                    listPr[i].setnume(listPr[j].getnume())
                    listPr[i].setadresa(listPr[j].getadresa())
                    listPr[i].setlisteven(listPr[j].getlisteven())

                    listPr[j].setidP(aux.getidP())
                    listPr[j].setnume(aux.getnume())
                    listPr[j].setadresa(aux.getadresa())
                    listPr[j].setlisteven(aux.getlisteven())

        return listPr