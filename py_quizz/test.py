import unittest
from classes.pregunta import Pregunta
from classes.quizz import Quizz

class TestPregunta(unittest.TestCase):
    def setUp(self):
        self.pregunta = Pregunta(pregunta="¿Cuanto es 2 + 2?", 
                                respuesta="4", opciones=["2", "5", "3"])
        self.pregunta2 = Pregunta(pregunta="¿Donde nacio Marie Curie?",
                                  respuesta="Polonia", opciones=["Francia", "Belgica", "Reino Unido"])
    
    def test_pregunta_correcta(self):
        self.assertEqual(self.pregunta.pregunta, "¿Cuanto es 2 + 2?")
        self.assertEqual(self.pregunta2.pregunta, "¿Donde nacio Marie Curie?")
    
    def test_pregunta_opciones_son_correctas(self):
        opciones= self.pregunta.obtener_opciones()
        self.assertIn("2", opciones)
        self.assertIn("3", opciones)
        self.assertIn("4", opciones)
        self.assertIn("5", opciones)

        opciones = self.pregunta2.obtener_opciones()
        self.assertIn("Polonia", opciones)
        self.assertIn("Francia", opciones)
        self.assertIn("Belgica", opciones)
        self.assertIn("Reino Unido", opciones)

    def test_da_respuesta_correcta(self):
        self.assertTrue(self.pregunta.es_correcto("4"))
        self.assertTrue(self.pregunta2.es_correcto("Polonia"))
    
    def test_da_respuesta_incorrecta(self):
        self.assertFalse(self.pregunta.es_correcto("5"))
        self.assertFalse(self.pregunta.es_correcto("3"))
        self.assertFalse(self.pregunta2.es_correcto("Francia"))
        self.assertFalse(self.pregunta2.es_correcto("Reino Unido"))


class TestQuizz(unittest.TestCase):
    def setUp(self):
        pregunta1 = Pregunta(pregunta="¿Cuanto es 2 + 2?", 
                                respuesta="4", 
                                opciones=["2", "5", "3"])
        pregunta2 = Pregunta(pregunta="¿Donde nacio Marie Curie?",
                                  respuesta="Polonia", 
                                  opciones=["Francia", 
                                            "Belgica", "Reino Unido"]
                                            )
        self.quizz = Quizz([pregunta1, pregunta2])
    
    def test_quizz_tiene_numero_preguntas_correctas(self):
        preguntas = self.quizz.obtener_preguntas()
        self.assertEqual(len(preguntas), 2)

    def test_quizz_me_da_pregunta(self):
        pregunta = self.quizz.siguiente_pregunta()
        self.assertTrue(type(pregunta) == Pregunta)
    
    def test_quizz_respoder_me_da_resultado_pregunta(self):
        pregunta = self.quizz.siguiente_pregunta()
        nueva_pregunta, resultado = self.quizz.responder(pregunta.respuesta)

        self.assertTrue(resultado)
        self.assertTrue(type(nueva_pregunta) == Pregunta)
        self.assertEqual(self.quizz.puntaje, 1)
    
    def test_quizz_responder_me_da_resultado_incorrecto(self):
        pregunta = self.quizz.siguiente_pregunta()
        nueva_pregunta, resultado = self.quizz.responder("respuesta incorrecta")

        self.assertFalse(resultado)
        self.assertTrue(type(nueva_pregunta) == Pregunta)
        self.assertEqual(self.quizz.puntaje, 0)

    def test_quizz_se_acaban_preguntas_correcto(self):
        pregunta = self.quizz.siguiente_pregunta()
        nueva_pregunta, resultado = self.quizz.responder(pregunta.respuesta)

        self.assertTrue(resultado)
        self.assertTrue(type(nueva_pregunta) == Pregunta)
        self.assertEqual(self.quizz.puntaje, 1)

        ultima_pregunta, resultado = self.quizz.responder(nueva_pregunta.respuesta)
        self.assertTrue(resultado)
        self.assertIsNone(ultima_pregunta)
        self.assertEqual(self.quizz.puntaje, 2)

    def test_quizz_se_acaban_preguntas_incorrecto(self):
        pregunta = self.quizz.siguiente_pregunta()
        nueva_pregunta, resultado = self.quizz.responder("incorrecto")

        self.assertFalse(resultado)
        self.assertTrue(type(nueva_pregunta) == Pregunta)
        self.assertEqual(self.quizz.puntaje, 0)

        ultima_pregunta, resultado = self.quizz.responder("incorrecto")
        self.assertFalse(resultado)
        self.assertIsNone(ultima_pregunta)
        self.assertEqual(self.quizz.puntaje, 0)

if __name__ == "__main__":
    unittest.main()