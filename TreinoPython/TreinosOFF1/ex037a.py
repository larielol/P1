num = int(input('Digite aqui o número: '))
print('Escolha a base: binária (B01), octal (O08) ou hexadecimal (H16).')
base = input('Digite a base para a conversão do número: ').upper()

if base == 'B01':
    binario = bin(num)
    print(f"O número digitado é {num} e a conversão binária é {num:b}.")
elif base == 'O08':
    octal = oct(num)
    print(f"O número digitado foi {num} e a conversão octal é {num:o}.")
elif base == 'H16':
    hexadecimal = hex(num)
    print(f"O número digitado foi {num} e a conversão hexadecimal é {num:x}.")
else:
    print(f"Base inválida, verifique e tente novamente.")