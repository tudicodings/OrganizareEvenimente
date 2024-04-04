from dataclasses import dataclass

@dataclass
class PersoanaDTO:
    nume: str
    adresa: str
    list_even: list

@dataclass
class EvenimentDTO:
    data: str
    timp: str
    desc: str
    cnt: int

class PerosanaDTOAssembler:
    @staticmethod
    def create_persoana_dto(persoana):
        nume = persoana.getnume()
        adresa = persoana.getadresa()
        list_even = persoana.getlisteven()
        return PersoanaDTO(nume, adresa, list_even)

class EvenimentDTOAssembler:
    @staticmethod
    def create_eveniment_dto(eveniment):
        data = eveniment.getdata()
        timp = eveniment.gettimp()
        desc = eveniment.getdesc()
        cnt = eveniment.getcnt()
        return EvenimentDTO(data, timp, desc, cnt)


