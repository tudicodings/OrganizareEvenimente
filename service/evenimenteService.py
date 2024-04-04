from domain.evenimente import Evenimente


class EvenimenteService:
    def __init__(self, evenimenteRepository):
        # in EvenimenteService se va crea un nou EvenimenteRepository
        self.__EvenimenteRepository = evenimenteRepository

    def getALLe(self):
        # returneaza o lista cu toate evenimentele
        return self.__EvenimenteRepository.getALL()

    def adauga(self, ideven, data, timp, desc, cnt):
        # adauga un nou eveniment in dictionar daca acesta nu se afla in dictionar, altfel KeyError
        eveniment = Evenimente(ideven, data, timp, desc, cnt)
        self.__EvenimenteRepository.adaugae(eveniment)

    def modifica(self, ideven, datan, timpn, descn, cntn):
        #  modifica un eveniment daca se afla in dictionar, altfel KeyError
        evenn = Evenimente(ideven, datan, timpn, descn, cntn)
        self.__EvenimenteRepository.modificae(evenn)

    def sterge(self, ideven):
        # sterge un eveniment daca se afla in dictionar, altfel KeyError
        self.__EvenimenteRepository.sterge(ideven)

    def findByid(self, ideven):
        # in cazul in care exista un eveniment cu id-ul dat il returneaza, altfel None
        self.__EvenimenteRepository.getByid(ideven)

    def signEvenid(self, ideven):
        # verifica daca exista un eveniment in dictionar dupa id-ul dat si creste cu 1 nr de eveninente inscrise
        # altfel KeyError
        # if self.findByid(ideven) is None:
        #   raise KeyError("Nu exista eveniment cu id-ul dat!")
        eveniment = self.__EvenimenteRepository.getByid(ideven)
        even_insc = int(eveniment.getcnt())
        even_insc += 1
        self.modifica(ideven, eveniment.getdata(), eveniment.gettimp(), eveniment.getdesc(), even_insc)

    def signEvenS(self):
        # returneaza o lista de evenimente sortata alfabetic dupa descriere
        listEven = self.__EvenimenteRepository.getALL()
        aux = Evenimente("0", "0", "0", "0", 0)
        for i in range(0, len(listEven) - 1):
            for j in range(i + 1, len(listEven)):
                if listEven[i].getdesc() > listEven[j].getdesc():
                    aux.setidE(listEven[i].getidE())
                    aux.setdata(listEven[i].getdata())
                    aux.settimp(listEven[i].gettimp())
                    aux.setdesc(listEven[i].getdesc())
                    aux.setcnt(listEven[i].getcnt())

                    listEven[i].setidE(listEven[j].getidE())
                    listEven[i].setdata(listEven[j].getdata())
                    listEven[i].settimp(listEven[j].gettimp())
                    listEven[i].setdesc(listEven[j].getdesc())
                    listEven[i].setcnt(listEven[j].getcnt())

                    listEven[j].setidE(aux.getidE())
                    listEven[j].setdata(aux.getdata())
                    listEven[j].settimp(aux.gettimp())
                    listEven[j].setdesc(aux.getdesc())
                    listEven[j].setcnt(aux.getcnt())

        return listEven

    def twp(self):
        listEven = self.__EvenimenteRepository.getALL()
        aux = Evenimente("0", "0", "0", "0", 0)

        for i in range(0, len(listEven) - 1):
            for j in range(i + 1, len(listEven)):
                if listEven[i].getcnt() < listEven[j].getcnt():
                    aux.setidE(listEven[i].getidE())
                    aux.setdata(listEven[i].getdata())
                    aux.settimp(listEven[i].gettimp())
                    aux.setdesc(listEven[i].getdesc())
                    aux.setcnt(listEven[i].getcnt())

                    listEven[i].setidE(listEven[j].getidE())
                    listEven[i].setdata(listEven[j].getdata())
                    listEven[i].settimp(listEven[j].gettimp())
                    listEven[i].setdesc(listEven[j].getdesc())
                    listEven[i].setcnt(listEven[j].getcnt())

                    listEven[j].setidE(aux.getidE())
                    listEven[j].setdata(aux.getdata())
                    listEven[j].settimp(aux.gettimp())
                    listEven[j].setdesc(aux.getdesc())
                    listEven[j].setcnt(aux.getcnt())

        rez = []
        lrez = (20 * len(listEven)) // 100
        lrez += 1
        for i in range(0, lrez):
            rez.append(listEven[i])

        return rez
