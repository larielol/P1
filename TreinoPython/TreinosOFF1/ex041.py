nascimento = int(input('Informe o ano de nascimento do atleta: '))

idade = 2022 - nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos e pertence a categoria MIRIM!')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem {idade} anos e pertence a categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'O atleta tem {idade} anos e pertence a categoria JUNIOR!')
elif idade > 19 and idade <= 20:
    print(f'O atleta tem {idade} anos e pertence a categoria SÊNIOR!')
else:
    print(f'O atleta tem {idade} anos e pertence a categoria MASTER!')
