from typing import List
from soma import SomaCalculadora
from subtracao import SubtracaoCalculadora
from multiplicacao import MultiplicacaoCalculadora
from divisao import DivisaoCalculadora
from calculadora_base import CalculadoraBase

def calcular(operacoes: List[CalculadoraBase], x, y) -> None:
    for operacao in operacoes:
        operacao.executa_operacao(x, y)

if __name__ == '__main__':
    calcular(
        [SomaCalculadora(),
        SubtracaoCalculadora(),
        MultiplicacaoCalculadora(),
        DivisaoCalculadora()], x=10, y=2)