nome = input('Digite aqui seu nome completo: ').strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculas é", nome.upper(),".")
print("Seu nome em minúsculas é", nome.lower(),".")
print(f"Seu nome tem", len(nome) - nome.count(" ") ,"letras.")
print("Seu primeiro nome tem", nome.find(" ") ,"letras.")
separa = nome.split()
print("Seu primeiro nome é", separa[0], "e ele tem", len(separa[0]), "letras.")