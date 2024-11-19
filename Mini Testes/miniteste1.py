#Ciência da Computação - Prog1
#Lucas Ariel Alves de Carvalho - 121210801

numero = int(input())
max = 0
min = 0
cont = 0
for n in range(0, numero):
    dados = int(input())
    cont += dados
    media = cont/(n+1)

    if dados > max:
        max = dados

    if dados > min:
        min = dados

    print(f"{dados} {min} {media:.2f} {max}")
