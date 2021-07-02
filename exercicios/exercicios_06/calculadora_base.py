# https://refactoring.guru/design-patterns/factory-method/python/example

from abc import ABC, abstractclassmethod

class CalculadoraBase(ABC):

    def factory_method(self):
        pass

    @abstractclassmethod
    def calcular(self, x, y):
        pass
        
    def recupera_operacao(self):
        print(type(self).__name__)

    def executa_operacao(self, x, y):
        caluladora = self.factory_method()
        print(f"O resultado é {caluladora.calcular(x, y)}")