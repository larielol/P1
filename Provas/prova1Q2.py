def letrasrep(letras):
    for p in letras:
        if senha1[p] == senha2[p]:
            contletrasrep += 1
        elif senha1[p+1] == senha2[p+1]:
            cont
    return repetidas


senha1 = input()
senha2 = input()
contletrasnaorep = 0
contletrasrep = 0
for p in range(len(senha1) - 1):
    if senha1[0] == senha2[0]:
        print(f'{senha1[0]} coincide na posição 0')
        contletrasrep += 1
    else:
        contletrasnaorep += 1







    if senha1[0+1] == senha2[0+1]:
        print(f'{senha1[1]} coincidente na posição 1')
        contletrasrep += 1

    else:
        for i in range(len(senha2)):
            if senha2[i] == senha1[i]:
                print(f'{senha2[i]} coincidente na posição {i + 1}')
                contletrasrep += 1