precoA = float(input('Digite aqui o valor atual do produto: R$'))

desconto = (5 / 100) * precoA
precoN = precoA - desconto

print(f"O valor com 5% de desconto ficará: R${precoN}.")
print("-----------------------------------------------------------")

descontonovo = (precoA * 5) / 100
preconovo = precoA - descontonovo

print(f"O valor do produto com 5% de desconto, será: R${preconovo}.")