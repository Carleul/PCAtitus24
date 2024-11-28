VALOR = 7
contador = 1

tentativa = int(input('Tente acertar o número de 1 a 10:'))

if tentativa > 10 or tentativa < 1:
        print('não quer brincar não desce pro play.')
        exit()

while tentativa != VALOR:
        contador += 1
        tentativa = int(input('Tente novamente:'))

if contador == 1:
        print('De primeira!')
elif contador < 5 and contador != 1:
        print('Parabéns! você levou', contador, 'tentativas!')
else:
        print('Caramba, levou', contador, 'tentativas...')