print('-' * 50)
print('Analisador de Triângulos:')
print('-' * 50)

a = float(input('Lado A do triângulo: '))
b = float(input('Lado B do triângulo: '))
c = float(input('Lado C do triângulo: '))

if a < b+c and b < a+c and c < a+b:
    print('Os comprimentos dos lados podem formar um triângulo.')
    if a == b and a == c and b == c:
        print('É um triângulo equilátero: todos os lados são iguais.')
    elif a == b != c or a == c != b or b == c != a:
        print('É um triângulo isósceles: dois lados são iguais.')
    elif a != b and  a != c and b != c:
        print('É um triângulo escaleno: todos os lados são diferentes')

else:
    print('Os comprimentos dos lados não podem formar um triângulo')