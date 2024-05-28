def primo(valor: int) -> bool:
    if valor <= 1:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    else:
        return True
if primo(5):
    print('é primo')
else:
    print('não é primo')