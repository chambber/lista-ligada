from .no import No


class ListaLigada:
    def __init__(self):
        self.primeiro_no = None
        self.tamanho = 0
        self.__ultimo_no = None

    def __str__(self):
        no_atual = self.primeiro_no
        elementos = ''
        while no_atual:
            elementos += f'{no_atual.elemento} '
            no_atual = no_atual.proximo
        return elementos

    def inserir_elemento(self, elemento):
        novo_no = No(elemento)
        if self.esta_vazia():
            self.primeiro_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
        self.__ultimo_no = novo_no
        self.tamanho += 1

    def esta_vazia(self):
        return self.tamanho == 0

    def existe_elemento(self, elemento):
        no_atual = self.primeiro_no
        while no_atual:
            if elemento == no_atual.elemento:
                return True
            no_atual = no_atual.proximo
        return False

    def obter_no(self, posicao):
        no_atual = self.primeiro_no
        for i in range(1, posicao):
            if not no_atual:
                return None
            no_atual = no_atual.proximo
        return no_atual

    def obter_elemento(self, posicao):
        no = self.obter_no(posicao)
        return no.elemento if no else None

    def inserir_elemento_posicao(self, elemento, posicao):
        no_atual = self.primeiro_no
        for i in range(1, posicao - 1):
            if not no_atual or not no_atual.proximo:
                break
            no_atual = no_atual.proximo

        novo_no = No(elemento)
        if no_atual:
            no_atual.proximo = novo_no
        else:
            self.primeiro_no = novo_no
            self.__ultimo_no = novo_no
        self.tamanho += 1

    def indice(self, elemento):
        posicao = 0
        no_atual = self.primeiro_no
        while no_atual:
            posicao += 1
            if elemento == no_atual.elemento:
                return posicao
            no_atual = no_atual.proximo
        return 0

    def remover_elemento(self, elemento):
        no_atual = self.primeiro_no
        no_anterior = None
        while no_atual:
            if no_atual.proximo and no_atual.proximo.elemento == elemento:
                no_anterior = no_atual
            no_atual = no_atual.proximo
            if no_anterior:
                break
        if no_anterior.elemento:
            no_anterior.proximo = no_atual.proximo
