dias_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
meses_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mes_30 = [4, 6, 9, 11]
def pedir_data():
    while True:                                                             # o código nao está terminado ainda
        dia = int(input('Digite o dia: '))
        if dia not in dias_validos:
            print('Esse dia não existe...')
            continue
        else:
            break
    while True:
        mes = int(input('Digite o mes: '))
        if mes not in meses_validos:
            print('Esse mês não existe...')
            continue
        if dia == 31 and (mes in mes_30 or mes == 2):
            print('Esse mês não tem 31 dias...')
            continue

        ano = int(input('Digite o ano: '))

        return dia, mes, ano

print('Você deverá informar a data inicial')
data_inicial = pedir_data()

def calcular_dias():
    global dias_do_mes
    for month in range(mes):
        if month in mes_30:
            dias_do_mes += 30
        elif month == 2:
            dias_do_mes += 28
        elif month == 2 and ano % 4 == 0:
            dias_do_mes += 29
        else:
            dias_do_mes += 31

    bissexto = ano % 4
    ano -= bissexto
    dias_do_ano = ano * 365 + bissexto * 366

    return dias_do_ano, dias_do_mes

dias_data_inicial = dia + dias_do_ano + dias_do_mes

print('Agora, a data atual')
data_atual = pedir_data()
calcular_dias()
dias_data_atual = dia + dias_do_ano + dias_do_mes

print('Por fim, a data final')
data_final = pedir_data()
calcular_dias()
dias_data_final = dia + dias_do_ano + dias_do_mes