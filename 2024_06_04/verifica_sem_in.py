def verifica_sem_in(lista: list, valor: int) -> bool:
    contador = 0
    for elemento in lista:
        contador += 1
        if elemento == valor:
            return True
        if contador == valor:
            return False
    return False

print(verifica_sem_in([1, 2, 3, 4, 5], 2))