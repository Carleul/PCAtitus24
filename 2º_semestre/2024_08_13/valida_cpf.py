def valida_cpf(cpf):
    chars_validos = []
    for i in range(10):
        chars_validos.append(i)
    pontos = cpf.count('.')
    traco = cpf.count('-')
    if pontos != 2:
        return False
    if traco != 1:
        return False
    numeros = cpf.split('.')
    final = numeros[2].split('-')
    tres = [numeros[0], numeros[1], final[0]]
    dois = final[1]
    for num in tres:
        if len(num) != 3:
            return False
    if len(dois) != 2:
        return False
    return True

print(valida_cpf('123.456.789-10'))
print(valida_cpf('123.456.789'))
print(valida_cpf('123.456.789-10 '))