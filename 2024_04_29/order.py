import random
lista = []
for x in range(10):
        n = random.randint(1,100)
        lista.append(n)
print('Lista aleatória ->', lista)
l = len(lista)
for i in range(l):
        for j in range(l - 1):
                if lista[j] > lista[j + 1]:
                        aux = lista[j]
                        lista[j] = lista[j + 1]
                        lista[j + 1] = aux
print('Lista ordenada ->', lista)