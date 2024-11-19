valor = float(input('Valor do produto: '))
print('Formas de pagamento: DI (dinheiro ou cheque à vista), CTA (cartão à vista), CT2 (cartão em 2x) e CT3 (cartão em 3x).')
forma = input('Forma de pagamento: ').upper()
if forma == 'DI':
    valor1 = (valor * 10) / 100
    valor11 = valor - valor1
    print(f'A forma de pagamento selecionada foi dinheiro ou cheque e ganhou 10% de desconto, seu valor será: R${valor11}.')
elif forma == 'CTA':
    valor1 = (valor * 5) / 100
    valor11 = valor - valor1
    print(f'A forma de pagamento selecionada foi cartão à vista e ganhou 5% de desconto, seu novo valor será: R${valor11}.')
elif forma == 'CT2':
    parcela = valor / 2
    print(f'A forma de pagamento selecionada foi cartão em 2x, valor para pagamento: R${valor}.')
    print(f'O parcelamento será em duas vezes de R${parcela}!')
elif forma == 'CT3':
    valor1 = (valor * 20) / 100
    valor11 = valor + valor1
    parcela = valor11 / 3
    print(f'A forma de pagamento selecionada foi cartão em 3x com juros de 20%, seu novo valor a ser pago será: R${valor11}.')
    print(f'O parcelamento será em três vezes de R${parcela}!')
else:
    print('Forma de pagamento não reconhecida, por favor, tente novamente.')
