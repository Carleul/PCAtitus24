def soma_pares(numeros: list, alvo: int) -> bool:
    for char1 in numeros:
        for char2 in numeros:
            if char1 + char2 == alvo:
                return True

    return False

print(soma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))