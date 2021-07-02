from calculadora_base import CalculadoraBase

class MultiplicacaoCalculadora(CalculadoraBase):    
    def calcular(self, x, y):
        self.recupera_operacao()
        return x * y            
        
    def factory_method(self):
        return MultiplicacaoCalculadora()