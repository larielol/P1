def contador(i, f, p):
    if p == 0:
        p = 1
    if i < f:
        for c in range(i, f+1, p):
            print(f'{c}', end=' ')
        print('Fim')
    else:
        for c in range(i, f-1, -p):
            print(f'{c}', end=' ')
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input())
fim = int(input())
pulo = int(input())
contador(inicio, fim, pulo)

