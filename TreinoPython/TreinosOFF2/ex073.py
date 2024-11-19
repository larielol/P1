times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-PR',
         'Flamengo', 'Inernacional', 'Atlético-MG', 'Bragantino',
         'Santos', 'São Paulo', 'Goiás', 'Botafogo', 'América-MG',
         'Ceará SC', 'Coritiba', 'Avaí', 'Cuiabá', 'Atlético-GO',
         'Juventude', 'Fortaleza')
print(f'Times do brasileirosão: {times}')
print('-' * 50)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-' * 50)
print(f'Os quatro últimos são: {times[-4:]}')
print('-' * 50)
print(f'{sorted(times)}')
print('-' * 50)
print(f'Bragantino está na posição {times.index("Bragantino") + 1}°')
