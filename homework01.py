distancia = float(input('digite sua distancia em km: '))
velocidade = float(input('digite sua velocidade em km/h: '))

tempo_total = distancia / velocidade

horas = int(tempo_total)

minutos = int((tempo_total - horas) * 60)

print(f'O tempo de viagem é {horas} hora(s) e {minutos} minuto(s).')
