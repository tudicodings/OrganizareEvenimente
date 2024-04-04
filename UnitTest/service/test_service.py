import unittest

from repository.evenimenteRepository import EvenimenteRepository
from repository.persoaneRepository import PersoaneRepository
from service.evenimenteService import EvenimenteService
from service.persoaneService import PersoaneService


class TestEvenimenteService(unittest.TestCase):
    def setUp(self):
        self.evenimentRepository = EvenimenteRepository
        self.evenimentService = EvenimenteService(self.evenimentRepository)
        self.evenimentService.adauga("1", "data", "timp", "descriere", 1)
        self.evenimentService.adauga("2", "data", "timp", "descriere", 3)

    def test_getALL(self):
        evenimente = self.evenimentService.getALLe()
        self.assertEqual(evenimente[0].getidE(), "1")
        self.assertEqual(evenimente[1].getidE(), "2")

    def test_addE(self):
        self.evenimentService.adauga("25", "data", "timp", "descriere", 3)
        evenimente = self.evenimentService.getALLe()
        self.assertEqual(evenimente[2].getidE(), "25")

        try:
            self.evenimentService.adauga("25", "data", "timp", "descriere", 3)
            assert False
        except KeyError:
            assert True

    def test_modif(self):
        self.evenimentService.modifica("1", "dataN", "timpN", "descriereN", 2)
        evenimente = self.evenimentService.getALLe()
        self.assertEqual(evenimente[0].gettimp(), "timpN")

        try:
            self.evenimentService.modifica("444", "dataN", "timpN", "descriereN", 3)
            assert False
        except KeyError:
            assert True

    def test_ste(self):
        self.evenimentService.sterge("2")
        evenimente = self.evenimentService.getALLe()
        self.assertEqual(len(evenimente), 1)

        try:
            self.evenimentService.sterge("444344")
            assert False
        except KeyError:
            assert True

    def test_findby(self):
        eveniment = self.evenimentService.findByid("2")
        self.assertEqual(eveniment.gettimp(), "timp")
        self.assertEqual(eveniment.getdata(), "data")

        eveniment2 = self.evenimentService.findByid("1234")
        self.assertIsNone(eveniment2)


class TestPersoaneService(unittest.TestCase):
    def setUp(self):
        self.persoanaRepository = PersoaneRepository()
        self.evenimentRepository = EvenimenteRepository()
        self.persoanaService = PersoaneService()
        self.persoanaService.adauga("1", "alex", "rodnei", [1, 2])

    def test_getall(self):
        persoane = self.persoanaService.getALLp()
        self.assertEqual(persoane[0].getnume(), "alex")

    def test_adaug(self):
        persoane = self.persoanaService.getALLp()
        self.assertEqual(persoane[0].getidP(), "1")

        try:
            self.persoanaService.adauga("14", "tudor", "rodnei", [1, 2])
            assert False
        except KeyError:
            assert True

    def test_modif(self):
        self.persoanaService.modifica("1", "tudor", "obcini", [2])
        persoane = self.persoanaService.getALLp()
        self.assertEqual(persoane[0].getnume(), "tudor")
        self.assertEqual(persoane[0].getadresa(), "obcini")

        try:
            self.persoanaService.modifica("3", "daria", "zamca", [1, 2])
            assert False
        except KeyError:
            assert True

    def test_ster(self):
        self.persoanaService.sterge("1")
        persoane = self.persoanaService.getALLp()
        self.assertEqual(len(persoane), 0)

        try:
            self.persoanaService.sterge("324")
            assert False
        except KeyError:
            assert True

    def test_findby(self):
        persoana = self.persoanaService.findByid("1")
        self.assertEqual(persoana.getid(), "1")
        persoana2 = self.persoanaService.findByid("29")
        self.assertIsNone(persoana2)

    if __name__ == '__main__':
        unittest.main()