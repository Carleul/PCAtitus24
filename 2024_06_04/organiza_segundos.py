def organiza_horario(seg: int) -> str:
    segundos= 0
    minutos = 0
    horas = 0
    if seg <= 60:
        print(seg, 'segundos')
    if seg <= 3600 and seg > 60:
        minutos = seg // 60
        segundos = seg % 60
        print(minutos, 'minutos e', segundos, 'segundos')
    if seg > 3600:
        horas = seg // 3600
        minutos = seg // 60 - horas * 60
        segundos = seg % 60
        print(horas, 'horas,', minutos, 'minutos e', segundos, 'segundos')

print(organiza_horario(3702))