import unittest
from animal import Animal
from mamifero import Mamifero

class animal_test(unittest.TestCase):
    def test_se_crea_animal(self):
        # El animal debe de incluir su nombre, su sonido y la cantidad de crias que da
        animal = Animal("pajaro", "pio", 3)
        self.assertTrue(animal.nombre == "pajaro")
        self.assertTrue(animal.sonido == "pio")
        self.assertTrue(animal.crias == 3)

class MamiferoTest(unittest.TestCase):
    def setUp(self):
        self.mamifero = Mamifero("perro", "guau", 5)

    def test_mamifero_es_animal(self):
        self.assertTrue(issubclass(type(self.mamifero), Animal), f"El mamifero tiene tipo {type(self.mamifero)} no es {Animal}")
        self.mamifero.nombre = "gato"
        self.assertEqual(self.mamifero.nombre, "gato")
        self.assertNotEqual(self.mamifero.nombre, "perro")
    
    def test_animal_es_perro(self):
        self.assertEqual(self.mamifero.nombre, "perro")

    def test_mamifero_hace_ruido(self):
        self.assertEqual(self.mamifero.hacer_ruido(), "guau")
        self.assertIsNot(self.mamifero.sonido, "x")
        esto_es_none = None
        self.assertIsNone(None)
        self.assertIn("p", self.mamifero.nombre)
        self.assertFalse(type(self.mamifero) == str)

if __name__ == "__main__":
    unittest.main()