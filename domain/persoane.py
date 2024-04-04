class Persoane:
    def __init__(self, idP, nume, adresa, list_even = []):
        # se vor atribui valori variabilelor din clasa Persoane
        self.__idP = idP
        self.__nume = nume
        self.__adresa = adresa
        self.__list_even = list_even

    def getidP(self):
        # returneaza id-ul persoanei
        return self.__idP

    def getnume(self):
        # returneaza numele persoanei
        return self.__nume

    def getadresa(self):
        # returneaza adresa persoanei
        return self.__adresa

    def getlisteven(self):
        # returneaza lista de evenimente la care persoana s-a inscris
        return self.__list_even

    def setidP(self, idP):
        # atribuie un nou id
        self.__idP = idP

    def setnume(self, nume):
        # atribuie un nume nou
        self.__nume = nume

    def setadresa(self, adresa):
        # atribuie o adresa noua
        self.__adresa = adresa

    def setlisteven(self, list_even):
        # atribuie o noua lista de evenimente la care persoana s-a inscris
        self.__list_even = list_even

    def __str__(self):
        # returneaza un sir de caractere care contine toate variabilele persoanei impreuna cu valorile lor
        return f"id: {self.__idP,}, nume: {self.__nume}, adresa: {self.__adresa}, evenimenteInscrise:{self.__list_even}"
