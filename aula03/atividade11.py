#Relembre seus tempos de escola e construa um programa que gere a tabuada completa de
# qualquer número que você escolher. O programa deve exibir os resultados da
# multiplicação do número escolhido por 1, 2, 3, até 10.
numero = int(input('Digite um numero:'))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')