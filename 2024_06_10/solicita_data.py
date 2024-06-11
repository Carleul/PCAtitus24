import datetime

data = input('informe uma data (dd/mm/aaaa): ')

data_obj = datetime.datetime.strptime(data, '%d/%m/%Y').date()

def data_organizada(data: datetime.date) -> str:
    return data.strftime('%m/%d/%y')

def linha_do_tempo(data):
    if data == datetime.date.today():
        return 'essa é a data atual.'
    elif data > datetime.date.today():
        return 'essa data é no futuro.'
    else:
        return 'essa data é no passado.'

def dia_semana(data_obj):
    return data_obj.strftime('esse dia é %A')

def finde(data_obj):
    if data_obj.weekday() < 5:
        return 'faltam ' + str(5 - data_obj.weekday()) + ' dias para o fim de semana.'
    if data_obj.weekday() == 5 or 6:
        return 'é fim de semana!'


def diferenca_dias(data_obj):
    if data_obj > datetime.date.today():
        diferenca = data_obj - datetime.date.today()
        return 'existe uma diferença de ' + str(diferenca.days) + ' dias entre essa data e a atual'
    elif data_obj < datetime.date.today():
        diferenca = datetime.date.today() - data_obj
        return 'existe uma diferença de ' + str(diferenca.days) + ' dias entre essa data e a atual'
    else:
        return 'não existe diferença pois essa é a data atual'

def proximo_mes(data_obj):
    return 'essa data no próximo mês será: ' + str(data_obj.day) + '/' + str(data_obj.month+1) + '/'  + str(data_obj.year)


print(data_organizada(data_obj))
print(linha_do_tempo(data_obj))
print(dia_semana(data_obj))
print(finde(data_obj))
print(diferenca_dias(data_obj))
print(proximo_mes(data_obj))