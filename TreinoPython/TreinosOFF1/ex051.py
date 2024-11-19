first = int(input('Primeiro termo: '))
second = int(input('Razão: '))
ten = first + (10-1) * second
for c in range(first, ten, second):
    print(f'{c}', end= ' -> ')
print('Finish!')