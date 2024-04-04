class Evenimente:
    def __init__(self, idE, data, timp, desc, cnt = 0):
        # se vor atribui valori variabilelor din clasa Evenimente
        self.__idE = idE
        self.__data = data
        self.__timp = timp
        self.__desc = desc
        self.__cnt = cnt

    def getidE(self):
        # returneaza id-ul evenimentului
        return self.__idE

    def getdata(self):
        # returneaza data evenimentului
        return self.__data
    
    def gettimp(self):
        # returneaza timpul evenimentului
        return self.__timp

    def getdesc(self):
        # returneaza descrierea evenimentului
        return self.__desc

    def getcnt(self):
        # returneaza numarul evenimentului inscris
        return self.__cnt

    def setidE(self, idE):
        # atribuie un nou id
        self.__idE = idE

    def setdata(self, data):
        # atribuie o data noua
        self.__data = data

    def settimp(self, timp):
        # atribuie un timp nou
        self.__timp = timp

    def setdesc(self, desc):
        # atribuie o descriere noua
        self.__desc = desc

    def setcnt(self, cnt):
        # atribuie o noua valoare pt numarul de evenimente inscrise
        self.__cnt = cnt

    def __str__(self):
        # returneaza un sir de caractere care contine toate variabilele evenimentului impreuna cu valorile lor
        return f"id: {self.__idE}, data: {self.__data}, timp: {self.__timp}, desc: {self.__desc}, inscriere: {self.__cnt}"

