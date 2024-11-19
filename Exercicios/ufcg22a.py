# Programação 1, 2021.2
# Solução de "Entre os extremos"
# lucas.ariel.carvalho@ccc.ufcg.edu.br

lista_numeros = []
maior = menor = 0
while True:
    num = input()
    if num == 'fim':
        break
    valores = num.split()
    for i in range(len(valores)):
        if int(valores[i]) != 'fim':
            lista_numeros.append(int(valores[i]))
maior = lista_numeros[0]
menor = lista_numeros[-1]
if maior < menor:
    maior = lista_numeros[-1]
    menor = lista_numeros[0]
print(f'{maior} {menor}')
for n in range(len(lista_numeros)):
    if menor < lista_numeros[n] < maior:
        print(lista_numeros[n])
