valorhoras = int(input("Valor horas? "))
quanthoras = int(input('Quantidade de horas? '))

salariobruto = valorhoras * quanthoras

if salariobruto <= 900:
    inss = salariobruto * 10 / 100
    fgts = salariobruto * 11 / 100
    totald = inss
    sl = salariobruto - totald
    print(f'Salário bruto: ({valorhoras} * {quanthoras})  : R$ {salariobruto:.2f}')
    print(f'(-) IR (Isento)')
    print(f'(-) INSS (10%)            : R$ {inss:.2f}')
    print(f'FGTS (11%)                : R$ {fgts:.2f}')
    print(f'Total de descontos        : R$ {totald:.2f}')
    print(f'Salário Líquido           : R$ {sl:.2f}')
elif salariobruto <= 1500:
    ir = salariobruto * 5 / 100
    inss = salariobruto * 10 / 100
    fgts = salariobruto * 11 / 100
    totald = inss + ir
    sl = salariobruto - totald
    print(f'Salário bruto: ({valorhoras} * {quanthoras})  : R$ {salariobruto:.2f}')
    print(f'(-) IR (5%)               : R$ {ir:.2f}')
    print(f'(-) INSS (10%)            : R$ {inss:.2f}')
    print(f'FGTS (11%)                : R$ {fgts:.2f}')
    print(f'Total de descontos        : R$ {totald:.2f}')
    print(f'Salário Líquido           : R$ {sl:.2f}')
elif salariobruto <= 2500:
    ir = salariobruto * 10 / 100
    inss = salariobruto * 10 / 100
    fgts = salariobruto * 11 / 100
    totald = inss + ir
    sl = salariobruto - totald
    print(f'Salário bruto: ({valorhoras} * {quanthoras})   : R$ {salariobruto:.2f}')
    print(f'(-) IR (10%)              : R$ {ir:.2f}')
    print(f'(-) INSS (10%)            : R$ {inss:.2f}')
    print(f'FGTS (11%)                : R$ {fgts:.2f}')
    print(f'Total de descontos        : R$ {totald:.2f}')
    print(f'Salário Líquido           : R$ {sl:.2f}')
else:
    ir = salariobruto * 20 / 100
    inss = salariobruto * 10 / 100
    fgts = salariobruto * 11 / 100
    totald = inss + ir
    sl = salariobruto - totald
    print(f'Salário bruto: ({valorhoras} * {quanthoras})   : R$ {salariobruto:.2f}')
    print(f'(-) IR (20%)              : R$ {ir:.2f}')
    print(f'(-) INSS (10%)            : R$ {inss:.2f}')
    print(f'FGTS (11%)                : R$ {fgts:.2f}')
    print(f'Total de descontos        : R$ {totald:.2f}')
    print(f'Salário Líquido           : R$ {sl:.2f}')