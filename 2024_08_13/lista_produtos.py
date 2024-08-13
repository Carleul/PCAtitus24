def busca_ingredientes(item: str, lista: list)-> str:
    lista_padronizada = []
    produtos_selecionados = []
    for ingrediente in lista:
        lista_padronizada.append(ingrediente.lower())
    item.lower()
    for produto in lista_padronizada:
        if item in produto:
            produtos_selecionados.append(produto)
    return produtos_selecionados

print(busca_ingredientes('queijo', ['requeijão', 'queijo Mozzarela', 'Queijo']))