from documento_fiscal import DocumentoFiscal


class Cpf(DocumentoFiscal):
    def __init__(self):
        super().__init__(range(10, 0, -1), range(11, 0, -1))

    def calcula_digito_verificador(self, documento, digito=1):
        documento = documento = self.retorna_digitos(documento)
        resultado = (self.recupera_soma_produtos(documento, digito) * 10) % 11
        return 0 if resultado == 10 else resultado
