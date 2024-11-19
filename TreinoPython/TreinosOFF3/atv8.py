salario = float(input('Digite seu salário: '))

if salario <= 280.00:
    salario1 = (salario * 20) / 100
    salario3 = salario1 + salario
    print(f'Seu salario recebeu um aumento de 20%')
    print(f'Valor antigo: R${salario:.2f}')
    print(f'O valor do aumento foi: R${salario1}')
    print(f'Valor atual: R${salario3:.2f}.')
elif salario > 280.00 and salario <= 700.00:
    salario1 = (salario * 15) / 100
    salario3 = salario1 + salario
    print(f'Seu salario recebeu um aumento de 15%')
    print(f'Valor antigo: R${salario:.2f}')
    print(f'O valor do aumento foi: R${salario1}')
    print(f'Valor atual: R${salario3:.2f}.')
elif salario > 700.00 and salario <= 1500.00:
    salario1 = (salario * 10) / 100
    salario3 = salario1 + salario
    print(f'Seu salario recebeu um aumento de 10%')
    print(f'Valor antigo: R${salario:.2f}')
    print(f'O valor do aumento foi: R${salario1}')
    print(f'Valor atual: R${salario3:.2f}.')
else:
    salario1 = (salario * 5) / 100
    salario3 = salario1 + salario
    print(f'Seu salario recebeu um aumento de 5%')
    print(f'Valor antigo: R${salario:.2f}')
    print(f'O valor do aumento foi: R${salario1}')
    print(f'Valor atual: R${salario3:.2f}.')


