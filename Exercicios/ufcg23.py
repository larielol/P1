def maior(alvo, inteiros):
    cont = 0
    lista = ''
    if inteiros != 'fim':
        inteiros = inteiros.split()
        for i in range(len(inteiros)):
            if inteiros[i] != 'fim':
                if int(inteiros[i]) > alvo:
                    cont += 1

        if cont > (len(inteiros) // 2):
            for ele in inteiros:
                if ele != inteiros[-1]:
                    lista += str(ele) + ' '
                else:
                    lista += str(ele)
            return lista
    else:
        return 0


def main():
    alvo = int(input())
    sequencia = 1
    while True:
        inteiros = input()
        if inteiros == 'fim': break
        valores = maior(alvo, inteiros)
        if valores != None:
            print(f'Sequência {sequencia}: {valores}')
        sequencia += 1

if name == 'main':
    main()