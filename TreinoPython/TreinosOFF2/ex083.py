lista = []
cont1 = cont2 = 0
exp = input('Digite sua expressão: ')
for s in exp:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
