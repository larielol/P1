from datetime import date

ano = int(input('Digite aqui o ano que queira analisar ou digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')

