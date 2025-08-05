def listar_sh(lista):

    tam_sh = len(lista)
    for i in range(tam_sh):
        print(f'[{i}] - {lista[i][0]} - {lista[i][1]}')

lista_sh = [['Hulk', 'Super força'], ['Batman', 'Dinheiro']]

while True:
    print('#### Sistema de Super Hero ####')
    print('1 - Cadastrar um super hero')
    print('2 - Alterar um super hero')
    print('3 - Deletar um super hero')
    print('4 - Listar um super hero')
    print('0 - Sair do sitema')

    op = int(input('Digite a opção desejada:'))

    if op == 1:
        print(' Cadastrou um super hero')
        nome = input('Digite o nome do super hero:')
        skill = input('Digite o skill do super hero:')
        lista_sh.append([nome, skill])

    elif op == 2:
        print(' Alterou um super hero')
        listar_sh()
        op_alt = int(input('Dgite o heroi a ser alterado: '))
        nome = input('Digite o nome do super hero:')
        skill = input('Digite o skill do super hero:')
        lista_sh[op_alt] = [nome, skill]
    elif op == 3:
        print(' Deletou um super hero')
        listar_sh()
        op_del = int(input('Dgite o heroi a ser deletado: '))
        del lista_sh[op_del]
    elif op == 4:
        print('### Lista de super heros ###')
        listar_sh()
    elif op == 0:
        print(' Saindo do sistema')
        break
    else:
        print('Digite uma opção válida')
