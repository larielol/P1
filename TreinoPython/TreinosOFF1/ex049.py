from time import sleep

num = int(input('Digite um número: '))

for n in range(1, 11):
    sleep(1)
    print(f'{num} x {n} = {num * n}')