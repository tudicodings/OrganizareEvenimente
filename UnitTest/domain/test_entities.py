import unittest
from domain.evenimente import *
from domain.persoane import *


class TestEvenimenteGet(unittest.TestCase):
    def setUp(self):
        self.eveniment = Evenimente("1", "data", "timp", "descriere", 1)

    def test_id_get(self):
        self.assertTrue(self.eveniment.getidE() == "1", "Id-ul trebuie sa fie: 1")

    def test_data_get(self):
        self.assertTrue(self.eveniment.getdata() == "data", "Data trebuie sa fie: data")

    def test_timp_get(self):
        self.assertTrue(self.eveniment.gettimp() == "timp", "Timpul trebuie sa fie: timp")

    def test_desc_get(self):
        self.assertTrue(self.eveniment.getdesc() == "descriere", "Descrierea trebuie sa fie: descriere")

    def test_cnt_get(self):
        self.assertTrue(self.eveniment.getcnt() == 1, "Contorul de inscrieri trebuie sa fie: 1")


class TestPersoaneGet(unittest.TestCase):
    def setUp(self):
        self.persoana = Persoane("1", "Nume", "Adresa", [1, 2])

    def test_id_get(self):
        self.assertTrue(self.persoana.getidP() == "1", "Id-ul trebuie sa fie: 1")

    def test_nume_get(self):
        self.assertTrue(self.persoana.getnume() == "Nume", "Numele trebuie sa fie: Nume")

    def test_adresa_get(self):
        self.assertTrue(self.persoana.getadresa() == "Adresa", "Adresa trebuie sa fie: Adresa")

    def test_lista_get(self):
        self.assertTrue(self.persoana.getlisteven() == [1, 2], "Lista trebuie sa fie: [1, 2]")

class TestEvenimenteSet(unittest.TestCase):
    def setUp(self):
        self.eveniment = Evenimente("1", "data", "timp", "descriere", 1)

    def test_id_set(self):
        self.eveniment.setidE("2")
        self.assertTrue(self.eveniment.getidE() == "2", "Id-ul trebuie sa fie: 2")

    def test_data_set(self):
        self.eveniment.setdata("data2")
        self.assertTrue(self.eveniment.getdata() == "data2", "Data trebuie sa fie: data2")

    def test_timp_set(self):
        self.eveniment.settimp("timp2")
        self.assertTrue(self.eveniment.gettimp() == "timp2", "Timpul trebuie sa fie: timp2")

    def test_desc_set(self):
        self.eveniment.setdesc("descriere2")
        self.assertTrue(self.eveniment.getdesc() == "descriere2", "Descrierea trebuie sa fie: descriere2")

    def test_cnt_set(self):
        self.eveniment.setcnt(2)
        self.assertTrue(self.eveniment.getcnt() == 2, "Contorul de inscrieri trebuie sa fie: 2")


class TestPersoaneSet(unittest.TestCase):
    def setUp(self):
        self.persoana = Persoane("1", "Nume", "Adresa", [1, 2])

    def test_id_set(self):
        self.persoana.setidP("2")
        self.assertTrue(self.persoana.getidP() == "2", "Id-ul trebuie sa fie: 2")

    def test_nume_set(self):
        self.persoana.setnume("daria")
        self.assertTrue(self.persoana.getnume() == "daria", "Numele trebuie sa fie: daria")

    def test_adresa_set(self):
        self.persoana.setadresa("rodnei")
        self.assertTrue(self.persoana.getadresa() == "rodnei", "Adresa trebuie sa fie: rodnei")

    def test_lista_set(self):
        self.persoana.setlisteven([1, 2, 3])
        self.assertTrue(self.persoana.getlisteven() == [1, 2, 3], "Lista trebuie sa fie: [1, 2, 3]")

    if __name__ == "__main__":
        unittest.main()


# class TestEvenimenteStr(unittest.TestCase):
#    def setUp(self):
#       self.eveniment = Evenimente("1", "data", "timp", "descriere", 1)
#
#   def test_str(self):
#       self.assertTrue(str(self.eveniment) == "id: 1 data: data timp: timp desc: descriere inscriere: 1 ", "Eveniment str trebuie sa fie 'id: 1 data: data timp: timp desc: descriere inscriere: 1'")


