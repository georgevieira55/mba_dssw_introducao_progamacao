PI = 3.14
altura = float(input('Digite o valor da altura:'))
raio = float(input('Digite o valor do raio:'))

area_lateral = 2 * PI * altura + raio
base = altura *(raio ** 2)
area_cilindro = area_lateral + base
qtd_litros = area_cilindro/3
qtd_latas = qtd_litros/8
custo_total = qtd_latas * 50

print(f'O custo total da pintura é RS{custo_total:.2f}')
