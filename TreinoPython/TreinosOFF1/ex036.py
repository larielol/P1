valorcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do salário? '))
anos = int(input('Em quantos anos irá pagar? '))

prestacao = (valorcasa / anos) / 12
porcentagem = (salario / 100) * 30

print(f"\nO valor da prestação do imóvel por mês é R${prestacao:.2f}")
print(f"30% do seu salário equivale à R${porcentagem:.2f}")

if prestacao <= porcentagem:
    print(f'\nVocê está apto para a compra do imóvel!')
else:
    print(f'\nVocê não está apto para a compra do imóvel!')