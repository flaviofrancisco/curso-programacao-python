from abc import ABC, abstractclassmethod
from typing import List

class Pessoa(ABC):
    @abstractclassmethod
    def recupera_nome(self):
        pass    

class Gerente(Pessoa):
    def recupera_nome(self):
        print('Nome do(a) gerente')


class Diretor(Pessoa):
    def recupera_nome(self):
        print('Nome do diretor(a)')    


def mostra_nome(pessoas: List[Pessoa]) -> None:
    for p in pessoas:
        p.recupera_nome()


mostra_nome([Gerente(), Diretor()])         