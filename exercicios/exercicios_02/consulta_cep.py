# https://viacep.com.br/
import requests, json

class ConsultaCep:

    url_base = 'https://viacep.com.br/ws/'

    def recupera_endereco(self, logradouro=None, cep=None, uf=None, cidade=None):
        if (cep != None):
            response = requests.get(f"{self.url_base}{'{}/json'.format(cep)}")
            return response.json()
        elif (logradouro != None and uf != None and cidade != None):
            response = requests.get(
                f"{self.url_base}{'{}/{}/{}/json'.format(uf, cidade, logradouro)}")
            return response.json()

    @classmethod
    def recupera_endereco_rj(cls, logradouro=None):
        return cls.recupera_endereco(cls,logradouro=logradouro, uf='RJ', cidade='Rio de Janeiro')            

response = ConsultaCep.recupera_endereco_rj(logradouro='Lúcio Costa')
# print(json.dumps(response, sort_keys=True, indent=4))   

print(response[0]['cep'])
