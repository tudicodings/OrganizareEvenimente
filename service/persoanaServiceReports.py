from repository.evenimenteRepository import EvenimenteRepository
from repository.persoaneRepository import PersoaneRepository
from domain.dto import *


class ReportsService:
    def __init__(self, persoaneRepository: PersoaneRepository, evenimenteRepository: EvenimenteRepository):
        self.__persoaneRepository = persoaneRepository
        self.__evenimenteRepository = evenimenteRepository

    def ordM(self):
        persoane_dto = self.__create_persoana_dto()
        persoane_dto = sorted(persoane_dto, key = lambda x: x.list_even, reverse= True)
        return persoane_dto

    def twp(self):
        evenimente_dto = self.__create_eveniment_dto()
        evenimente_dto = sorted(evenimente_dto, key = lambda x: x.cnt, reverse = True)
        rez = (20 * len(evenimente_dto)) // 100
        rez += 1
        return evenimente_dto[:rez]

    def __create_persoana_dto(self):
        persoane_dto = []
        for persoana in self.__persoaneRepository.getALL():
            dto = PerosanaDTOAssembler.create_persoana_dto(persoana)
            persoane_dto.append(dto)
        return persoane_dto

    def __create_eveniment_dto(self):
        evenimente_dto = []
        for eveniment in self.__evenimenteRepository.getALL():
            dto = EvenimentDTOAssembler.create_eveniment_dto(eveniment)
            evenimente_dto.append(dto)
        return evenimente_dto
