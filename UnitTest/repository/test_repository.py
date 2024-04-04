import unittest

from domain.evenimente import Evenimente
from domain.persoane import Persoane
from repository.evenimenteRepository import EvenimenteRepository
from repository.persoaneRepository import PersoaneRepository


class TestEvenimenteRepository(unittest.TestCase):
    def setUp(self):
        self.evenimentRepository = EvenimenteRepository()
        self.eveniment1 = Evenimente("1", "9.12", "1", "film", 1)
        self.eveniment2 = Evenimente("2", "10.12", "1.30", "teatru", 2)
        self.evenimentRepository.adaugae(self.eveniment1)
        self.evenimentRepository.adaugae(self.eveniment2)

    def test_getALL(self):
        evenimente = self.evenimentRepository.getALL()
        self.assertTrue(len(evenimente) == 2, "Valoare incorecta")
        self.assertTrue(evenimente[0].getidE() == "1", "Id-ul primului eveniment trebuie sa fie: 1")
        self.assertTrue(evenimente[1].getidE() == "2", "Id-ul evenimentului nr2 trebuie sa fie: 2")

    def test_getbyId(self):
        eveniment1 = self.evenimentRepository.getByid("1")
        self.assertEqual(eveniment1.getdata(), "9.12")

        eveniment2 = self.evenimentRepository.getByid("2")
        self.assertEqual(eveniment2.getdata(), "10.12")

    def test_addEveniment(self):
        eveniment = Evenimente("3", "9.12", "95", "film", 7)
        self.evenimentRepository.adaugae(eveniment)
        evenimente = self.evenimentRepository.getALL()
        self.assertEqual(evenimente[2].getidE(), "3")

        try:
            self.evenimentRepository.adaugae(self.eveniment1)
            assert False
        except KeyError:
            assert True

    def test_update(self):
        eveniment = Evenimente("2", "10.12", "1", "teatru", 2)
        self.evenimentRepository.modificae(eveniment)
        evenimente = self.evenimentRepository.getALL()
        self.assertEqual(evenimente[0].gettimp(), "1")

        try:
            eveniment_nou = Evenimente("5", "10.12", "1", "teatru", 2)
            self.evenimentRepository.modificae(eveniment_nou)
            assert False
        except KeyError:
            assert True

    def test_delete(self):
        self.evenimentRepository.sterge(self.eveniment1.getidE())
        evenimente = self.evenimentRepository.getALL()
        self.assertEqual(evenimente[0].getidE(), "2")

        try:
            self.evenimentRepository.sterge("324")
            assert False
        except KeyError:
            assert True

class TestPersoaneRepository(unittest.TestCase):
    def setUp(self):
        self.persoanaRepository = PersoaneRepository()
        self.persoana1 = Persoane("1", "tudor", "rodnei", [1, 2])
        self.persoana2 = Persoane("2", "daria", "rodnei", [2])
        self.persoanaRepository.adauga(self.persoana1)
        self.persoanaRepository.adauga(self.persoana2)

    def test_getALL(self):
        persoane = self.persoanaRepository.getALL()
        self.assertTrue(len(persoane) == 2, "Valoare incorecta!")
        self.assertTrue(persoane[0].getidP() == "1", "Id-ul primei persoane trebuie sa fie: 1")
        self.assertTrue(persoane[1].getnume() == "daria", "Numele persoanei 2 trebuie sa fie: daria")

    def test_getbyID(self):
        persoana1 = self.persoanaRepository.getByid("1")
        self.assertEqual(persoana1.getadresa(), "rodnei")

        persoana2 = self.persoanaRepository.getByid("2")
        self.assertEqual(persoana2.getlisteven(), [2])

    def test_addPersoana(self):
        persoana = Persoane("3", "alex", "zamca", [1, 2, 3])
        self.persoanaRepository.adauga(persoana)
        persoane = self.persoanaRepository.getALL()
        self.assertEqual(persoane[2].getidP, "3")

        try:
            self.persoanaRepository.adauga(self.persoana1)
            assert False
        except KeyError:
            assert True

    def test_update(self):
        persoana = Persoane("2", "mark", "obc", [1])
        self.persoanaRepository.modifica(persoana)
        persoane = self.persoanaRepository.getALL()
        self.assertEqual(persoane[0].getnume(), "tudor")

        try:
            persoana_noua = Persoane("5", "mark", "obc", [1])
            self.persoanaRepository.modifica(persoana_noua)
            assert False
        except KeyError:
            assert True


    if __name__ == "__main__":
        unittest.main()