from soma import SomaCalculadora
from subtracao import SubtracaoCalculadora
from multiplicacao import MultiplicacaoCalculadora
from divisao import DivisaoCalculadora
from calculadora_base import CalculadoraBase

def calcular(calculadora: CalculadoraBase, x, y):  
    calculadora.executa_operacao(x, y)
    print('Fim cálculo ...')
    pass

if __name__ == '__main__':
    calcular(SomaCalculadora(), 10, 2)
    calcular(SubtracaoCalculadora(), 10, 2)
    calcular(MultiplicacaoCalculadora(), 10, 2)
    calcular(DivisaoCalculadora(), 10, 2)
