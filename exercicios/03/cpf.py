from documento_fiscal import DocumentoFiscal

class Cpf(DocumentoFiscal):
    def __init__(self):
        self.__NUM_DV1 = range(10, 0, -1)        
        self.__NUM_DV2 = range(11, 0, -1)

    def calcula_digito_verificador(self, cnpj, digito=1):
        pesos = self.__NUM_DV1 if digito == 1 else self.__NUM_DV2
        resultado = (sum(int(digito) * peso for digito,peso in zip(cnpj, pesos))) % 11
        resultado = (resultado * 10) % 11
        return 0 if resultado == 10 else resultado
