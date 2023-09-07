base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))
perimetro = 2*(base + altura)
area = base * altura
diagonal = (base**2 + altura**2)**0.5
print(f"Perimetro: {perimetro}")
print(f"area: {area}")
print(f"diagonal: {diagonal:.2f}")
