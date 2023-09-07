salarioM = int(input("Entre com o salário minimo: "))
qw = int(input("Entre com a quantidade de quilowatt: "))
preco = salarioM/700
vp = preco*qw
vd = vp * 0.9
print(f"\nPreço do quilowatt: {preco:.2f}, valor a ser pago> {vp:.2f}")
print(f"Valor com desconto: {vd:.2f}")
