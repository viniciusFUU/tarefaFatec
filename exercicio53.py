base = float(input("Entre com a base: "))
altura = float(input("Entre com a altura: "))
profundidade = float(input("Entre com a profundidade: "))
diagonal = (base**2 + altura**2 + profundidade**2)**0.5
print(f"Diagonal: {diagonal:.2f}")
