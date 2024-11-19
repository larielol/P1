# Programação 1, 2021.2
# Solução de "Milheiro de Tijolos"
# lucas.ariel.carvalho@ccc.ufcg.edu.br

soma = fornada = 0
lista_tijolos = []

while True:
    tijolo = int(input())
    soma += tijolo
    fornada += 1
    lista_tijolos.append(tijolo)
    if soma >= 1000:
        break

media = soma/fornada
media1 = 0

for tijolo in lista_tijolos:
    if tijolo > media:
        media1 += 1

print(f'{soma}')
print(f'{media:.2f}')
print(f'{media1}')