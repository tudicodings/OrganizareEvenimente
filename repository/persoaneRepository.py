class PersoaneRepository:
    def __init__(self):
        # se va crea un dictionar pentru a stoca datele persoanei
        self.__persoane = {}

    def getALL(self):
        # returneaza o lista cu toate persoanele
        return list(self.__persoane.values())

    def getByid(self, idP):
        # in cazul in care exista o persoana cu un id dat o returneaza, altfel None
        if idP in self.__persoane:
            return self.__persoane[idP]
        return None

    def adauga(self, persoana):
        # adauga o noua persoana daca aceasta nu se afla deja in dictionar, altfel KeyError
        if self.getByid(persoana.getidP()) is not None:
            raise KeyError("Exista deja o persoana cu id-ul dat!")
        self.__persoane[persoana.getidP()] = persoana

    def modifica(self, persoanaN):
        # modifica o persoana daca se afla in dictionar, altfel KeyError
        if self.getByid(persoanaN.getidP()) is None:
            raise KeyError("Nu exista nicio persoana cu id-ul dat!")
        self.__persoane[persoanaN.getidP()] = persoanaN

    def sterge(self, idpers):
        # sterge o persoana dupa un id dat daca se afla in dictionar, altfel KeyError
        if idpers is None:
            raise KeyError("Nu exista nicio persoana cu id-ul dat!")
        self.__persoane.pop(idpers)
