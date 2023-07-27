# -*- coding:UTF-8 -*-

class No:

    def __init__(self, chave=None, dado=None):
        self.__chave = chave
        self.__dado = dado


    @property
    def dado(self):
        return self.__dado


    @dado.setter
    def dado(self, valor):
        self.__dado = valor


    @property
    def chave(self):
        return self.__chave
    

    @chave.setter
    def chave(self, valor):
        self.__chave = valor


    def __str__(self) -> str:
        return f"Chave: {self.__chave}; Dado: {self.__dado}"