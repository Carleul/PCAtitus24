def organiza_nome(nome: str):
    nome_organizado = ''
    for letter in nome:
        if not (letter.isalpha() or ' '):
            return False
        if letter.isnumeric():
            return False
    if ' ' not in nome:
        return False
    if nome == '':
        return None
    lista_nome = nome.split()
    for name in lista_nome:
        nome_organizado += name.capitalize() + ' '

    return nome_organizado

print(organiza_nome('carlo guterres'))