from cnpj import Cnpj
from cpf import Cpf

if __name__ == '__main__':
    validaCnpj = Cnpj()
    cnpj = input('Informe um CNPJ: ')
    print(validaCnpj.valido(cnpj))
    cnpj = validaCnpj.retorna_digitos(cnpj)
    dv1 = validaCnpj.calcula_digito_verificador(cnpj[:12], 1)
    dv2 = validaCnpj.calcula_digito_verificador(cnpj[:12] + str(dv1), 2)
    print(f'Dígito verificador 1: {dv1} e dígito verificador 2: {dv2}')

    validaCpf = Cpf()
    cpf = input('Informe um CPF: ')
    print(validaCpf.valido(cpf))
    cpf = validaCpf.retorna_digitos(cpf)
    dv1 = validaCpf.calcula_digito_verificador(cpf[:9], 1)
    dv2 = validaCpf.calcula_digito_verificador(cpf[:9] + str(dv1), 2)
    print(f'Dígito verificador 1: {dv1} e dígito verificador 2: {dv2}')
