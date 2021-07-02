from calculadora_base import CalculadoraBase

class SubtracaoCalculadora(CalculadoraBase):    
    def calcular(self, x, y):
        self.recupera_operacao()
        return x - y            
        
    def factory_method(self):
        return SubtracaoCalculadora()