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

    def obter_no(self, posicao):
        no_atual = self.primeiro_no
        for i in range(posicao):
            if not no_atual:
                return None
            no_atual = no_atual.proximo
        return no_atual

    def obter_elemento(self, posicao):
        no = self.obter_no(posicao)
        return no.elemento if no else None

    def indice(self, elemento):
        no_atual = self.primeiro_no
        for i in range(self.tamanho):
            if elemento == no_atual.elemento:
                return i
            no_atual = no_atual.proximo
        return -1

    def contem(self, elemento):
        indice = self.indice(elemento)
        return indice > -1

    def inserir_posicao(self, posicao, elemento):
        if posicao >= self.tamanho:
            self.inserir_elemento(elemento)
            return

        no_alterior = None
        no_atual = self.primeiro_no
        for i in range(posicao):
            no_alterior = no_atual
            no_atual = no_atual.proximo

        novo_no = No(elemento, no_atual)
        if no_alterior:
            no_alterior.proximo = novo_no
        else:
            self.primeiro_no = novo_no
        self.tamanho += 1

    def remover_elemento(self, elemento):
        no_atual = self.primeiro_no
        no_anterior = None
        while no_atual:
            if no_atual.proximo and no_atual.proximo.elemento == elemento:
                no_anterior = no_atual
            no_atual = no_atual.proximo
            if no_anterior:
                break
        if no_anterior:
            no_anterior.proximo = no_atual.proximo
