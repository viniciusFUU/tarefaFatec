import math as m
pr1 = float(input("Digite a nota da prova 1: "))
pr2 = float(input("Digite a nota da prova 2: "))
mf = (pr1+pr2)/2

print(f"Média truncada = {round((mf - 0.5)+0.001)}")
print(f"Média arredondada = {round(mf+0.001)}")
