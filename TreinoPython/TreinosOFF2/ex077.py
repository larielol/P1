palavras = ('Amor', 'Fofa', 'Dente', 'Saude', 'Momolete', 'Placa',
            'Importante', 'Aula', 'Gostei', 'Cuscuz', 'Pano', 'Gato',
            'Cachorro', 'Mamute', 'Internet', 'Linda', 'Lux', 'Shampoo',
            'Arroz', 'Linguagem', 'Python', 'Hora', 'Soluvel', 'Disco')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra in 'AEIOUaeiou':
            print(letra, end=' ')