from repository.evenimenteFileRepository import EvenimenteFileRepository
# from repository.evenimenteRepository import EvenimenteRepository
from repository.persoaneFileRepository import PersoaneFileRepository
# from repository.persoaneRepository import PersoaneRepository
from service.evenimenteService import EvenimenteService
from service.persoanaServiceReports import ReportsService
from service.persoaneService import PersoaneService
from ui.console import Consola


def main():
    # persoaneRepository = PersoaneRepository()
    persoaneRepository = PersoaneFileRepository("persoaneFis")
    # evenimenteRepository = EvenimenteRepository()
    evenimenteRepository = EvenimenteFileRepository("/Users/tudorr/PycharmProjects/orgevenimente/evenimenteFis")
    persoaneService = PersoaneService(persoaneRepository, evenimenteRepository)
    evenimenteService = EvenimenteService(evenimenteRepository)
    rapoarteService = ReportsService(persoaneRepository, evenimenteRepository)
    consola = Consola(persoaneService, evenimenteService, rapoarteService)

    consola.meniu()



if __name__ == "__main__":
    main()
