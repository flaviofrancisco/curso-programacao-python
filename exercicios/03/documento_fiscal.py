class DocumentoFiscal:
    def __init__(self):
        self.__NUM_DV1 = []
        self.__NUM_DV2 = []

    def calcula_digito_verificador(self, documento, digito=1):
        pass

    def valido(self, documento):
        documento = documento.replace('.', '').replace('/', '').replace('-', '')

        if (not documento.isnumeric()):
            return False

        digitos = None

        if (len(documento) == 11):
            digitos = documento[:9]
        elif (len(documento) == 14):
            digitos = documento[:12]
        else:
            return False             

        dv1 = self.calcula_digito_verificador(digitos)
        dv2 = self.calcula_digito_verificador(digitos + str(dv1), 2)

        return documento == digitos + str(dv1) +str(dv2)
