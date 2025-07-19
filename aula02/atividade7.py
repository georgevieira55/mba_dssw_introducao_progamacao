print('--- Iniciando o programa ---')

temperatura = float(input('informe a temperatura: '))

print('1 - Celsius')
print('2 - Fahrenheit')
escala = int(input('Digite a escala'))

if escala == 1:
    temperatura = temperatura * 1.8 + 32
    print(f'A temperatura {temperatura} em celsius')
    print(f'Ficou {temperatura} em Fahrenheit')

elif escala == 2:
    temperatura = (temperatura - 32) / 1.8
    print(f'A temperatura {temperatura} em celsius')
    print(f'Ficou {temperatura} em Fahrenheit')


else:
    print(f'A opção {escala} é inválida')

print('--- Finaçizando o programa ---')