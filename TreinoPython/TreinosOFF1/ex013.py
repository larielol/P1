salarioF = float(input('Digite aqui o seu salário: R$'))

aumento = (15 /100) * salarioF
novosalario = aumento + salarioF

print(f"Seu salário R${salarioF} recebeu 15% de aumento, logo, ficará no valor: R${novosalario}.")

aumentonovo = (salarioF * 15) / 100
salarionovo = aumentonovo + salarioF

print(f"Seu salário R${salarioF} recebeu um aumento de 15%, logo, ficará: R${salarionovo}")
