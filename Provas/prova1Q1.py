# Programação 1, 2021.2
# Solução de "Altera Senha (Prova1)"
# lucas.ariel.carvalho@ccc.ufcg.edu.br

#1 = Antiga, 2 = Atual
senha1 = input()
senha2 = input()
contletrasrep = 0

menor = senha1
if len(senha1) > len(senha2):
    menor = senha2

for p in range(len(menor)):
    if senha1[p] == senha2[p]:
        print(f'{senha1[p]} coincidente na posição {p+1}')
        contletrasrep += 1

if contletrasrep >= 1:
        print(f'Senha não alterada')
else:
        print(f'Senha alterada com sucesso')