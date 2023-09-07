import math as m
num = int(input("Entre com um número de trÊs digitos: "))
c = num / 100
d = num % 100 / 10
u = num % 10
num1 = u*100 + d*10 + c
numInvertido = str(num)
# Não deu certo fazendo como no enunciado
print(
    f"O número selecionado foi: {num} e o número invertido é: {m.floor(num1)}")
# Fiz transformando o int em str e puxei as posições de maneira inversa
print(f"Número invertido corretamente: {numInvertido[2]}{numInvertido[1]}{numInvertido[0]}")
