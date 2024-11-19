num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

for i in range(len(num_ext)):
    if num >= 0 and num <= 20:
        numero = num_ext[num]
        print(f'Você digitou o número {numero}')
        break
    else:
        print('Tente novamente!')
        num = int(input('Digite um número entre 0 e 20: '))