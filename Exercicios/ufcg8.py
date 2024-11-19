num1 = int(input())
num2 = int(input())
soma = 0

for n in range(num1, num2 + 1):
    if n % 2 != 0:
        soma += n
print(soma)