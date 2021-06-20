class DocumentoFiscal:
    def __init__(self, numeros_dv1, numeros_dv2):
        self.__NUM_DV1 = numeros_dv1
        self.__NUM_DV2 = numeros_dv2

    def retorna_digitos(self, documento):
        return documento.replace('.', '').replace('/', '').replace('-', '')

    def calcula_digito_verificador(self, documento, digito=1):
        pass

    def recupera_soma_produtos(self, documento, digito=1):
        pesos = self.__NUM_DV1 if digito == 1 else self.__NUM_DV2
        resultado = (sum(int(digito) * peso for digito,peso in zip(documento, pesos)))
        return resultado

    def valido(self, documento):
        documento = self.retorna_digitos(documento)

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
