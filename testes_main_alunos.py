import unittest
from datetime import datetime
from app import obter_resposta


class TestObterResposta(unittest.TestCase):

    def test_saudacoes(self):
        self.assertEqual(obter_resposta("olá"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("boa tarde"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("bom dia"), "Olá tudo bem!")

    def test_perguntas_simples(self):
        self.assertEqual(obter_resposta("como estás"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("qual é a tua função?"), "A minha função é responder a perguntas simples.")
        self.assertEqual(obter_resposta("gostas de python?"), "Sim, Python é uma linguagem muito utilizada.")
        self.assertEqual(obter_resposta("o que é programação?"), "Programação é criar instruções para o computador executar.")

    def test_despedidas(self):
        self.assertEqual(obter_resposta("bye"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("adeus"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("tchau"), "Gostei de falar contigo! Até breve...")

    def test_ajuda_e_agradecimento(self):
        self.assertEqual(obter_resposta("ajuda"), "Podes perguntar como estou, as horas, a data ou outras perguntas simples.")
        self.assertEqual(obter_resposta("obrigado"), "De nada! Foi um prazer ajudar.")

    def test_horas_e_data(self):
        hora_atual = datetime.now().strftime("%H:%M")
        data_atual = datetime.now().strftime("%d-%m-%Y")

        self.assertEqual(obter_resposta("que horas são"), f"São: {hora_atual} horas")
        self.assertEqual(obter_resposta("qual é a data"), f"Hoje é dia: {data_atual}")

    def test_resposta_padrao(self):
        self.assertEqual(
            obter_resposta("xyz123"),
            "Desculpa, não entendi a questão! xyz123"
        )

        self.assertEqual(
            obter_resposta("teste123"),
            "Desculpa, não entendi a questão! teste123"
        )


if __name__ == '__main__':
    unittest.main()