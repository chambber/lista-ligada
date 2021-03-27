from unittest import TestCase

from listas.lista_ligada import ListaLigada


class TestListaLigada(TestCase):
    def setUp(self):
        self.lista = ListaLigada()


class TestInit(TestListaLigada):
    def test_initial_primeiro_no(self):
        self.assertIsNone(self.lista.primeiro_no)

    def test_initial_tamanho(self):
        self.assertEqual(self.lista.tamanho, 0)


class TestInserirElemento(TestListaLigada):
    def test_primeiro_no(self):
        self.lista.inserir_elemento(10)
        self.assertIsNotNone(self.lista.primeiro_no)
        self.assertIsNone(self.lista.primeiro_no.proximo)
        self.assertEqual(self.lista.tamanho, 1)

    def test_proximo_no(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.assertEqual(self.lista.primeiro_no.elemento, 1)
        self.assertIsNotNone(self.lista.primeiro_no.proximo)
        self.assertEqual(self.lista.primeiro_no.proximo.elemento, 2)
        self.assertIsNone(self.lista.primeiro_no.proximo.proximo)
        self.assertEqual(self.lista.tamanho, 2)


class TestEstaVazia(TestListaLigada):
    def test_inicio(self):
        self.assertTrue(self.lista.esta_vazia())

    def test_com_nos(self):
        self.lista.inserir_elemento(1)
        self.assertFalse(self.lista.esta_vazia())


class TestExisteElemento(TestListaLigada):
    def test_sem_nos(self):
        self.assertFalse(self.lista.existe_elemento(10))

    def test_sem_elemento(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.assertFalse(self.lista.existe_elemento(4))
        self.assertFalse(self.lista.existe_elemento(10))

    def test_com_elemento(self):
        self.lista.inserir_elemento(10)
        self.lista.inserir_elemento(20)
        self.lista.inserir_elemento(30)
        self.lista.inserir_elemento(40)
        self.assertTrue(self.lista.existe_elemento(10))
        self.assertTrue(self.lista.existe_elemento(20))
        self.assertTrue(self.lista.existe_elemento(30))
        self.assertTrue(self.lista.existe_elemento(40))


class TestObterNo(TestListaLigada):
    def test_sem_nos(self):
        self.assertIsNone(self.lista.obter_no(1))

    def test_sem_posicao(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.assertIsNone(self.lista.obter_no(4))
        self.assertIsNone(self.lista.obter_no(10))

    def test_com_posicao(self):
        self.lista.inserir_elemento(10)
        self.lista.inserir_elemento(20)
        self.lista.inserir_elemento(30)
        self.lista.inserir_elemento(40)
        self.assertIsNotNone(self.lista.obter_no(1))
        self.assertIsNotNone(self.lista.obter_no(2))
        self.assertIsNotNone(self.lista.obter_no(3))
        self.assertIsNotNone(self.lista.obter_no(4))


class TestObterElemento(TestListaLigada):
    def test_sem_nos(self):
        self.assertIsNone(self.lista.obter_elemento(1))

    def test_sem_posicao(self):
        self.lista.inserir_elemento(1)
        self.lista.inserir_elemento(2)
        self.lista.inserir_elemento(3)
        self.assertIsNone(self.lista.obter_elemento(4))
        self.assertIsNone(self.lista.obter_elemento(10))

    def test_com_posicao(self):
        self.lista.inserir_elemento(10)
        self.lista.inserir_elemento(20)
        self.lista.inserir_elemento(30)
        self.lista.inserir_elemento(40)
        self.assertEqual(self.lista.obter_elemento(1), 10)
        self.assertEqual(self.lista.obter_elemento(2), 20)
        self.assertEqual(self.lista.obter_elemento(3), 30)
        self.assertEqual(self.lista.obter_elemento(4), 40)
