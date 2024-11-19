num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f"O maior número digitado é: {num1}")
if num2 > num1 and num2 > num3:
    print(f"O maior número digitado é: {num2}")
if num3 > num1 and num3 > num2:
    print(f"O maior número digitado é: {num3}")

if num1 < num2 and num1 < num3:
    print(f"O menor número digitado é: {num1}")
if num2 < num1 and num2 < num3:
    print(f"O menor número digitado é: {num2}")
if num3 < num1 and num3 < num2:
    print(f"O menor número digitado é: {num3}")
else:
    print(f"Verifique os números digitados.")

