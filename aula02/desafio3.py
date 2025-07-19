altura = float(input('digite sua altura :'))
peso = float(input('digite sua peso :'))

imc = peso / (altura * altura)
print(imc)

if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso normal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 35:
    print('obesidade grau I')
elif 35 <= imc < 40:
    print("obesidade grau II")
elif 40 <= imc:
    print("obesidade grau III")

print(f'O IMC foi de {imc:.2f}')
