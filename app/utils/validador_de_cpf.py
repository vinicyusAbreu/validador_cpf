import re


def validandoCPF(cpf):
    if not isinstance(cpf, str):
        return False

    if bool(re.search('[a-zA-Z]', cpf)) or bool(re.search('[^\w\s.\-:()@&#]|:(?![()])|(?<!:)[()]', cpf)):
        return False

    if bool(re.search('(\d{3}).(\d{3}).(\d{3})(-{1})(?!-)(.*)', cpf)) or bool(re.search('(\d{3})(\d{3})(\d{3})(.*)', cpf)):
        pass
    else:
        return False

    cpf = re.sub("[^0-9]", '', cpf)

    if len(set(cpf)) == 1 or len(cpf) != 11:
        return False

    if not cpf.isdigit():
        return False

    soma = 0
    peso = 10

    for n in range(9):
        soma = soma + int(cpf[n]) * peso

        peso = peso - 1

    digitoVerificador = 11 - soma % 11

    if digitoVerificador > 9:
        primeirodigitoVerificador = 0
    else:
        primeirodigitoVerificador = digitoVerificador

    soma = 0
    peso = 11
    for n in range(10):
        soma = soma + int(cpf[n]) * peso

        peso = peso - 1

    digitoVerificador = 11 - soma % 11

    if digitoVerificador > 9:
        segundodigitoVerificador = 0
    else:
        segundodigitoVerificador = digitoVerificador

    if cpf[-2:] == f"{primeirodigitoVerificador}{segundodigitoVerificador}":

        return True

    return False
