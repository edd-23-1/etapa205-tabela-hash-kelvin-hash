# -*- coding:UTF-8 -*-
from no import No

class TabelaHashEnderecamentoAberto:

    #Constantes
    OCUPADO = 1
    VAZIO = -1
    LIBERADO = -2

    """
    Tabela Hash com tratamento de colisão por endereçamento aberto
    utilizando sondagem quadrática para resolver colisões
    """
    def __init__(self, tamanho=32):
        self.__tamanho = tamanho
        self.__tabela = [None] * tamanho
        self.__qtd = 0
        print(f"Criada EDD Tabela Hash com capacidade: {tamanho}")


    # Retorna o valor do hash para uma determinada chave
    def __hash(self, chave) -> int:
        # implementação do método
        return hash(chave) % self.__tamanho


    # Retorna o valor do hash2 para uma determinada chave e índice k
    def __hash2(self, chave, k) -> int:
        # implementação do método
        pass

    
    # Retorna a posição do objeto No na Tabela Hash para uma determinada chave
    # Caso a chave não exista na tabela, retorna -1
    # Esse é um método privado, pois só é utilizado dentro da classe
    # Ele é usado internamente para auxiliar os métodos get() e remove()
    def __find(self, chave) -> int:
        # implementação do método
        position = self.__hash(chave)

        for count in range(self.__tamanho):
            if (self.__tabela[position] is None
                or self.__tabela[position].chave == chave
                or self.__tabela[position].chave == self.LIBERADO):

                break

            position = self.__hash2(chave, count)

        if self.__tabela[position] is None or count >= self.__tamanho - 1:
            return -1

        return position


    # Retorna o objeto No da tabela hash para uma determinada chave
    # Caso a chave não exista na tabela, retorna None
    def get(self, chave) -> No:
        # implementação do método
        position = self.__find(chave)

        if position == -1:
            return None

        return self.__tabela[position].dado


    # Insere um nó na tabela hash recebendo uma chave e um valor
    # Caso a chave já exista na tabela, sobrescreve o valor
    # Caso a tabela esteja cheia, retorna False
    def insert(self, chave, valor) -> None:
        # implementação do método
        pass
    

    # Remove um dado da tabela inserindo None na posição da 
    # lista de chaves e da lista do valores
    # Retorna True se a remoção foi bem sucedida, False caso contrário
    def remove(self, chave) -> bool:
        # implementação do método
        pass

    
    # Retorna uma lista de tuplas com os seguintes valores: (chave, valor, status) 
    # Caso a posição não tenha sido ocupada, retorna a seguinte tupla: (None, None, status) 
    # Caso a tabela esteja vazia, retorna uma lista vazia
    def display(self) -> list[tuple]:
        # implementação do método
        pass


