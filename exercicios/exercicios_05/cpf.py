
from documento_base import DocumentoBase

class Cpf(DocumentoBase):
    def __init__(self):
        self._pesos_dv1 = range(10, 0, -1)
        # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self._pesos_dv2 = range(11, 0, -1)
        # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def calcula_digito_verificador(self, documento, digito=1):
        documento = self.retorna_digitos(documento)
        resultado = (self.recupera_soma_produtos(documento, digito) * 10) % 11
        return 0 if resultado == 10 else resultado
