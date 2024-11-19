num = int(input())
modulo = 10
divisao = 1
while True:
    i = num // divisao % modulo
    if i == 0:
        break
    print(i)
    divisao *= 10



# num / 1 % 10