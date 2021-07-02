from calculadora_base import CalculadoraBase

class DivisaoCalculadora(CalculadoraBase):    
    def calcular(self, x, y):
        self.recupera_operacao()
        return x / y            
        
    def factory_method(self):
        return DivisaoCalculadora()