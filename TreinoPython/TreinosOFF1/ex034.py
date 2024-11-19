salario = float(input('Digite o seu salário: '))

salario1 = (salario * 10) / 100
salario2 = (salario * 15) / 100

salario11 = salario + salario1
salario22 = salario + salario2

if salario <= 1.250:
    print(f'Seu salário recebeu um aumento de 15% e o novo valor mensal será: {salario22}')
else:
    print(f'Seu salário recebeu um aumento de 10% e o novo valor mensal será: {salario11}')
