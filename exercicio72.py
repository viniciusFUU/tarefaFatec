deposito=float(input("Entre com o depósito: "));
taxa=float(input("Entre com a taxa de juros: "));
valor=deposito*taxa/100;
total=deposito+valor;
print(f"Rendimentos: {valor}, Total: {total}");