from cnpj import Cnpj
from cpf import Cpf

validador = Cnpj()        
cnpj = input('Informe um CNPJ: ')
print(validador.valido(cnpj))
dv1 = validador.calcula_digito_verificador(cnpj[:12], 1)
dv2 = validador.calcula_digito_verificador(cnpj[:12] + str(dv1), 2)
print(f'Dígito verificador 1: {dv1} e dígito verificador 2: {dv2}')


validador = Cpf()        
cpf = input('Informe um CPF: ')
print(validador.valido(cpf))
dv1 = validador.calcula_digito_verificador(cpf[:9], 1)
dv2 = validador.calcula_digito_verificador(cpf[:9] + str(dv1), 2)
print(f'Dígito verificador 1: {dv1} e dígito verificador 2: {dv2}')
