from documento_base import DocumentoBase

class Cnpj(DocumentoBase):    
    def __init__(self): 
        self._pesos_dv1 = list(range(5, 1, -1)) + list(range(9, 1, -1))    
         #[5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        self._pesos_dv2 = list(range(6, 1, -1)) + list(range(9, 1, -1))     
         #[6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]          

    def calcula_digito_verificador(self, documento, digito=1):
        documento = self.retorna_digitos(documento)
        resultado = self.recupera_soma_produtos(documento, digito) % 11
        return 0 if resultado < 2 else 11 - resultado
