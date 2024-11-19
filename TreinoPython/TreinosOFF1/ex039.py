print('Bem vindo ao alistamento, digite abaixo seu ano de nascimento e o seu sexo (masculino ou feminino).')
nascimento = int(input('Ano do seu nascimento? '))
sexo = input('Seu sexo: ').lower().strip()
ano = 2022
idade = 2022 - nascimento
alistamento = nascimento + 18

if idade < 18 and sexo == 'masculino':
    print(f'Ainda não está no momento de se alistar, falta {18 - idade} ano(s) para o alistamento.')
    print(f'O ano para o seu alistamento será em {alistamento}.')
elif idade == 18 and sexo == 'masculino':
    print(f'É o momento de se alistar!')
elif idade > 18 and sexo == 'masculino':
    print(f'Já passou do momento de se alistar! Se passou {idade - 18} ano(s) do prazo de alistamento.')
    print(f'O ano do seu alistamento foi em {alistamento}.')
elif sexo == 'feminino':
    print(f'Alistamento obrigatório somente para o sexo masculino (homens)!')