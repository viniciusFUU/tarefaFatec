num = float(input("Entre com um numero com parte fracionária: "))
numI = round((num - 0.5))
numFrac = num - numI
numA = round(num + 0.00001)
print(f"A parte inteiro: {numI}")
print(f"A parte fracionada: {numFrac+0.00001:.4f}")
print(f"Número arredondado: {numA}")
