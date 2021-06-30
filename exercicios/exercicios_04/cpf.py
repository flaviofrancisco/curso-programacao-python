_pesos_dv1 = range(10, 0, -1)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
_pesos_dv2 = range(11, 0, -1)
# [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def _recupera_digito_verificador(digitos, digito):
    pesos = _pesos_dv1 if digito == 1 else _pesos_dv2
    digito_verificador1 = (
        (sum(int(digito) * peso for digito, peso in zip(digitos, pesos))) * 10) % 11
    return 0 if digito_verificador1 == 10 else digito_verificador1


def cpf_valido(documento):
    documento = documento.replace('.', '').replace('/', '').replace('-', '')
    if (not documento.isnumeric()):
        return False
    digitos = None
    if (len(documento) == 11):
        digitos = documento[:9]
    else:
        return False
    dv1 = _recupera_digito_verificador(digitos, 1)
    dv2 = _recupera_digito_verificador(digitos + str(dv1), 2)
    return documento == digitos + str(dv1) + str(dv2)
