import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_levanta_erro_caso_valor_passado_por_parametro_nao_for_int(self):
        with self.assertRaises(AssertionError):
           bacon_com_ovos('') 
           

    def test_passar_valor_multiplo_de_3_e_5_retorna_bacon_com_ovos(self):
        valores_entrada = (15, 30, 45, 60, 75)

        for entrada in valores_entrada:
            with self.subTest(entrada=entrada):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    'Bacon com Ovos',
                )


    def test_retornar_bacon_se_valor_for_multiplo_apenas_de_5(self):
        valores_entrada = (5, 10, 20, 40, 80)

        for entrada in valores_entrada:
            with self.subTest(entrada=entrada):
                self.assertEqual(bacon_com_ovos(entrada), 'Bacon')


    def test_retornar_ovos_se_valor_for_divisivel_apenas_por_3(self):
        valores_entrada = (3, 9, 12, 18, 21)

        for entrada in valores_entrada:
            with self.subTest(entrada=entrada):
                self.assertEqual(bacon_com_ovos(entrada), 'Ovos')


    def test_retorna_passar_fome_se_valor_nao_for_divisivel_nem_por_5_nem_por_3(self):
        valores_entrada = (2, 4, 8, 28)

        for entrada in valores_entrada:
            with self.subTest(entrada=entrada):
                self.assertEqual(bacon_com_ovos(entrada), 'Passar fome')
