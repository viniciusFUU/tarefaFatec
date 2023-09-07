nome = input("Entre com teu nome: ")
print(nome)
print(f"Primeiro caractere: {nome[0]}")
print(f"Último caractere: {nome[-1]}")
print(f"Do primeiro ao terceiro caractere: {nome[0:3]}")
print(f"Quarto caractere: {nome[3]}")
print(f"Todos os caracteres menos o primeiro: {nome[1:]}")
n = nome[-2]
print(f"Os dois últimos caracteres: {n}{nome[-1]}")
