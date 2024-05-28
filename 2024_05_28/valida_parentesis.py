def validador_parenteses(s: str) -> bool:
    contador = 0
    for char in s:
        if char == '(':
            contador += 1
        elif char == ')':
            contador -= 1
            if contador < 0:
                return False
    if contador == 0:
        return True
    else:
        return False


# Valores válidos
print(validador_parenteses('()'))
print(validador_parenteses('())('))
print(validador_parenteses('()()'))
print(validador_parenteses('(())'))
print(validador_parenteses('(()()())'))
print(validador_parenteses('(((())()))'))

# Valores inválidos
print(validador_parenteses(')'))
print(validador_parenteses('('))
print(validador_parenteses('()('))
print(validador_parenteses('()()())'))
print(validador_parenteses('(((())())'))