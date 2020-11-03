# Esta função retornará verdadeiro (True)
# se todos os números do CPF forem iguais.
def numeros_iguais(cpf):
    i = 0
    while i < len(cpf):
        if i != 0 and cpf[i - 1] != cpf[i]:
            return False
        i += 1
    return True


# Esta função serve para auxiliar no cálculo
# para retornar o primeiro ou segundo dígito.
# Para retornar o valor correto do primeiro dígito
# o parâmetro fator deve ser igual a: 10.
# Para o segundo dígito o fator deve ser igual a 11.
# f = fator
# n = dígitos do cpf
# (f - 1) * n1 + (f - 2) * n2 ....
def recupera_soma(cpf, fator):
    resultado = 0
    for i, n in enumerate(cpf[:9]):
        resultado += int(n) * fator
        fator -= 1
    return resultado


# Função que deverá retornar o
# primeiro dígito verificador do
# CPF informado.
def recupera_primeiro_digito(cpf):
    soma = recupera_soma(cpf, 10)
    resultado = (soma * 10) % 11
    if resultado == 10:
        return 0
    return resultado


# Função que deverá retornar o
# segundo dígito verificador do
# CPF informado.
def recupera_segundo_digito(cpf, primeiro_digito):
    soma = recupera_soma(cpf, 11)
    soma += (primeiro_digito * 2)
    resultado = (soma * 10) % 11
    return resultado

# Função que irá retornar verdadeiro se o CPF for válido.
def cpf_valido(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isnumeric() or numeros_iguais(cpf):
        return False
    digito1 = recupera_primeiro_digito(cpf)
    digito2 = recupera_segundo_digito(cpf, digito1)
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

# Função principal do módulo
# caso seja executado diretamente:
# $ python valida_cpf_02.py
if __name__ == '__main__':
    print('Informe o CPF')
    cpf = input()
    if cpf_valido(cpf):
        print('CPF é válido.')
    else:
        print('CPF inválido')
