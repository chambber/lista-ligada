from unittest import TestCase

from listas.lista_ligada import ListaLigada


class TestListaLigada(TestCase):
    def setUp(self):
        self.lista = ListaLigada()


class TestInit(TestListaLigada):
    def test_initial_primeiro_no(self):
        self.assertIsNone(self.lista.primeiro_no)

    def test_initial_tamanho(self):
        self.assertEqual(0, self.lista.tamanho)


class TestInserirElemento(TestListaLigada):
    def test_primeiro_no(self):
        self.lista.inserir_elemento(10)
        self.assertIsNotNone(self.lista.primeiro_no)
        self.assertIsNone(self.lista.primeiro_no.proximo)
        self.assertEqual(1, self.lista.tamanho)

    def test_proximo_no(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.assertEqual(self.lista.primeiro_no.elemento, 1)
        self.assertIsNotNone(self.lista.primeiro_no.proximo)
        self.assertEqual(self.lista.primeiro_no.proximo.elemento, 2)
        self.assertIsNone(self.lista.primeiro_no.proximo.proximo)
        self.assertEqual(2, self.lista.tamanho)


class TestEstaVazia(TestListaLigada):
    def test_inicio(self):
        self.assertTrue(self.lista.esta_vazia())

    def test_com_nos(self):
        self.lista.inserir_elemento(1)
        self.assertFalse(self.lista.esta_vazia())


class TestObterNo(TestListaLigada):
    def test_sem_nos(self):
        self.assertIsNone(self.lista.obter_no(0))

    def test_sem_posicao(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.assertIsNone(self.lista.obter_no(3))
        self.assertIsNone(self.lista.obter_no(10))

    def test_com_posicao(self):
        self.lista.inserir_elemento(10)
        self.lista.inserir_elemento(20)
        self.lista.inserir_elemento(30)
        self.lista.inserir_elemento(40)
        self.assertIsNotNone(self.lista.obter_no(0))
        self.assertIsNotNone(self.lista.obter_no(1))
        self.assertIsNotNone(self.lista.obter_no(2))
        self.assertIsNotNone(self.lista.obter_no(3))


class TestObterElemento(TestListaLigada):
    def test_sem_nos(self):
        self.assertIsNone(self.lista.obter_elemento(0))

    def test_sem_posicao(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.assertIsNone(self.lista.obter_elemento(3))
        self.assertIsNone(self.lista.obter_elemento(10))

    def test_com_posicao(self):
        self.lista.inserir_elemento(10)
        self.lista.inserir_elemento(20)
        self.lista.inserir_elemento(30)
        self.lista.inserir_elemento(40)
        self.assertEqual(10, self.lista.obter_elemento(0))
        self.assertEqual(20, self.lista.obter_elemento(1))
        self.assertEqual(30, self.lista.obter_elemento(2))
        self.assertEqual(40, self.lista.obter_elemento(3))


class TestContem(TestListaLigada):
    def test_sem_nos(self):
        self.assertFalse(self.lista.contem(10))

    def test_sem_elemento(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.assertFalse(self.lista.contem(4))
        self.assertFalse(self.lista.contem(10))

    def test_com_elemento(self):
        self.lista.inserir_elemento(10)
        self.lista.inserir_elemento(20)
        self.lista.inserir_elemento(30)
        self.lista.inserir_elemento(40)
        self.assertTrue(self.lista.contem(10))
        self.assertTrue(self.lista.contem(20))
        self.assertTrue(self.lista.contem(30))
        self.assertTrue(self.lista.contem(40))


class TestIndice(TestListaLigada):
    def test_sem_nos(self):
        self.assertEqual(-1, self.lista.indice(10))

    def test_sem_elemento(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.assertEqual(-1, self.lista.indice(4))
        self.assertEqual(-1, self.lista.indice(10))

    def test_com_elemento(self):
        self.lista.inserir_elemento(10)
        self.lista.inserir_elemento(20)
        self.lista.inserir_elemento(30)
        self.lista.inserir_elemento(40)
        self.assertEqual(0, self.lista.indice(10))
        self.assertEqual(1, self.lista.indice(20))
        self.assertEqual(2, self.lista.indice(30))
        self.assertEqual(3, self.lista.indice(40))


class TestInserirPosicao(TestListaLigada):
    def test_posicao_maior(self):
        self.lista.inserir_posicao(0, 1);
        self.assertEqual(0, self.lista.indice(1))
        self.assertEqual(1, self.lista.tamanho)

        self.lista.inserir_posicao(10, 2);
        self.assertEqual(1, self.lista.indice(2))
        self.assertEqual(2, self.lista.tamanho)

    def test_primeira_posicao(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.lista.inserir_elemento(4)
        self.lista.inserir_posicao(0, 0)
        self.assertEqual(0, self.lista.indice(0))
        self.assertEqual(1, self.lista.indice(1))
        self.assertEqual(2, self.lista.indice(2))
        self.assertEqual(3, self.lista.indice(3))
        self.assertEqual(4, self.lista.indice(4))
        self.assertEqual(5, self.lista.tamanho)

    def test_no_meio(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.lista.inserir_elemento(4)
        self.lista.inserir_posicao(3, 10)
        self.assertEqual(0, self.lista.indice(1))
        self.assertEqual(1, self.lista.indice(2))
        self.assertEqual(2, self.lista.indice(3))
        self.assertEqual(3, self.lista.indice(10))
        self.assertEqual(4, self.lista.indice(4))
        self.assertEqual(5, self.lista.tamanho)
