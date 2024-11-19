listagem = ('Abacaxi', 1.70,
            'Leite', 10,
            'Manga', 5,
            'Cenoura', 3,
            'Chá', 3.50,
            'Couve', 5.70,
            'Repolho', 4.90,
            'Acelga', 8,
            'Batata frita', 9.50)
for i in range(len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:<15}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')