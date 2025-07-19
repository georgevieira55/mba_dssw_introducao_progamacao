ladoA = 11
ladoB = 12
ladoC = 10

if ladoA == ladoB == ladoC:
    print('Triângulo equilátero')
elif ladoA != ladoB != ladoC:
    print('Triângulo escaleno')
elif(ladoA == ladoB != ladoC) or (ladoB == ladoC != ladoA or ladoC == ladoA != ladoB):
    print('Triângulo isoceles')
