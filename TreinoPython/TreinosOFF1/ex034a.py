salario = float(input('Qual o seu salário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f"Você ganhava R${salario:.2f}, passa a receber R${novo:.2f} agora.")
