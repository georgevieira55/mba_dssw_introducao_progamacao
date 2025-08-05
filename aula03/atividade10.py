from random import randint
import time

numero_aleatorio = randint(1, 100)
parada = True

while parada:

    meu_numero = int(input('digite um numero de 1 - 100:'))

    if meu_numero == numero_aleatorio:
        print('voce acertou!')
        parada = False

    elif meu_numero < numero_aleatorio:
        print('Seu numero é menor')

    elif meu_numero > numero_aleatorio:
        print('Seu numero é maior')

    time.sleep(1)

print('programa encerrado')

