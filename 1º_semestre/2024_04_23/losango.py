altura = int(input('insira um número ímpar e maior ou igual a três:'))

if altura % 2 == 0:
        altura += 1
        print('o valor digitado era par, usaremos', altura, 'no lugar.')

metade = altura // 2

for linha in range(metade + 1):
        espacos = metade - 1
        hashtag = (2 * linha) + 1
        print('.' * espacos + '#' * hashtag)

for linha in range(metade):
        espacos = 1 - linha
        hashtag = (altura - 2) - (2 * linha)
        print('.' * espacos + '#' * hashtag)