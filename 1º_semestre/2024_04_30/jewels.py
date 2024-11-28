contador = 0
jewels = 'x'
stones = input('Insira suas pedras:')
for char in stones:
    if char == jewels:
        contador += 1
if contador > 0:
    print('Existem', contador, 'jóias entre suas pedras')
else:
    print('não existem jóias entre suas pedras')