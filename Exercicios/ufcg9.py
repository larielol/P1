par = impar = 0
while True:
    num = input()
    if num == 'fim':
        break
    if int(num) % 2 == 0:
        par += 1
    else:
        impar += 1

if par > 0 or impar > 0:
    if impar == 0:
        print(f'pares = {par}')
    elif par == 0:
        print(f'impares = {impar}')
    else:
        print(f'pares = {par}')
        print(f'ímpares = {impar}')
