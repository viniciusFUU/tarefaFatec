p = float(input("Digite o valor da aplicação: "))
i = int(input("Digite a taxa (0-1): "))
m = int(input("Digite a quantidade de meses: "))
va = p*(((1 + i) ** m)-1)/i
print(f"O valor acumulado: {va}")
