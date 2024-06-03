def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input('digite o numero que deseja saber o fatorial:'))
print(factorial(n))

# essa calculadora de fatorial não aceita números negativos, afinal não existe fatorial de números negativos