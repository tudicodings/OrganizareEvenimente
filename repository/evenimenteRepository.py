class EvenimenteRepository:
    def __init__(self):
        # se va crea un dictionar pentru a stoca datele evenimentului
        self.__evenimente = {}

    def getALL(self):
        # returneaza o lista cu toate evenimentele
        return list(self.__evenimente.values())

    def getByid(self, idP):
        # in cazul in care exista un eveniment cu un id dat il returneaza, altfel None
        if idP in self.__evenimente:
            return self.__evenimente[idP]
        return None

    def adaugae(self, eveniment):
        # adauga un nou eveniment daca acesta nu se afla deja in dictionar, altfel KeyError
        if self.getByid(eveniment.getidE()) is not None:
            raise KeyError("Exista deja o persoana cu id-ul dat!")
        self.__evenimente[eveniment.getidE()] = eveniment

    def modificae(self, evenimentN):
        # modifica un eveniment daca se afla in dictionar, altfel KeyError
        if self.getByid(evenimentN.getidE()) is None:
            raise KeyError("Nu exista nicio persoana cu id-ul dat!")
        self.__evenimente[evenimentN.getidE()] = evenimentN

    def sterge(self, ideven):
        # sterge un eveniment dupa un id dat daca se afla in dictionar, altfel KeyError
        if self.getByid(ideven) is None:
            raise KeyError("Nu exista nicio persoana cu id-ul dat!")
        self.__evenimente.pop(ideven)
