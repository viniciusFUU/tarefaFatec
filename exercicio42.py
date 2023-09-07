import math as m

angulo = int(input("Digite ângulo em graus: "))
rang = angulo*3.14/180
print(f"Seno: {m.sin(rang)}")
print(f"Co-seno: {m.cos(rang)}")
print(f"Tangente: {m.tan(rang)}")
print(f"Co-secante: {1/ m.sin(rang)}")
print(f"Secante: {1/ m.cos(rang)}")
print(f"Cotangente: {1/ m.tan(rang)}")
