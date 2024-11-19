print('-' * 50)
print('Analisador de Triângulos:')
print('-' * 50)

a = float(input('Lado A do triângulo: '))
b = float(input('Lado B do triângulo: '))
c = float(input('Lado C do triângulo: '))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print('Os comprimentos dos lados podem formar um triângulo.')
else:
    print('Os comprimentos dos lados não podem formar um triângulo')
