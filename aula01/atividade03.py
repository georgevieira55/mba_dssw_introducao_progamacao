valordoproduto= float(input('Digite o valor do produto:'))
percentualdedesconto= float(input('Digite o valor do desconto:'))

valorcomdesconto = (valordoproduto * percentualdedesconto)
valorfinal = (valordoproduto - valorcomdesconto)

print ( f' O valorfinal é {valorfinal : .2f}')