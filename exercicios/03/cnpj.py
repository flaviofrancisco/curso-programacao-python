from documento_fiscal import DocumentoFiscal

class Cnpj(DocumentoFiscal):
    def __init__(self):
        self.__NUM_DV1 = list(range(5, 1, -1)) + list(range(9, 1, -1))
        #[5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        self.__NUM_DV2 = list(range(6, 1, -1)) + list(range(9, 1, -1))
        #[6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def calcula_digito_verificador(self, cnpj, digito=1):
        pesos = self.__NUM_DV1 if digito == 1 else self.__NUM_DV2
        resultado = (sum(int(digito) * peso for digito,peso in zip(cnpj, pesos))) % 11
        return 0 if resultado < 2 else 11 - resultado
