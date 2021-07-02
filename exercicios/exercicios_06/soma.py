from calculadora_base import CalculadoraBase

class SomaCalculadora(CalculadoraBase):    
    def calcular(self, x, y):
        self.recupera_operacao()
        return x + y            
        
    def factory_method(self):
        return SomaCalculadora()