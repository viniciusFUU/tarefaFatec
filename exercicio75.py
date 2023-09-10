peso = int(input("Entre com teu peso, só a parte inteira: "))
pesograma = peso*1000
novoPeso = round(pesograma*1.12)
print(f"Peso em gramas: {pesograma}")
print(f"Novo peso: {novoPeso/1000}Kg")
