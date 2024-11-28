ano = int(input('insira um ano: '))

if ano % 4 == 0:
        print('esse ano é bissexto!')
else:
        p_ano = ano + (4 - ano % 4)
        print('esse ano não é bissexto, mas o próximo bissexto será', p_ano)