num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print ('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opcao = int(input('1, 2, 3, 4 ou 5? '))

    if opcao == 1:
        soma = num1 + num2
        print(f'{soma} é a soma dos números.')
    elif opcao == 2:
        multiplicacao = num1 * num2
        print(f'{multiplicacao} é a multipicação dos números')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é o maior número')
        else:
            print(f'{num2} é o maior número')
    elif opcao == 4:
        num1n = int(input('Primeiro número: '))
        num1 = num1n
        num2n = int(input('Segundo número: '))
        num2 = num2n
    else:
        print('Opção inválida, tente novamente!')
    print('-' * 50)

print('.')