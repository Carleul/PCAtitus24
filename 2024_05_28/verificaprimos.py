def primo(valor: int) -> bool:
    if valor <= 1:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    else:
        return True
def lista_primos(valor: int) -> list:
    lista_primos = []
    for i in range(valor + 1):
        if primo(i):
            lista_primos.append(i)
    return lista_primos

num = int(input('Digite um valor, vou mostrar os números primos que existem até ele: '))
print(lista_primos(num))