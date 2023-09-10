qtd = int(input("Digite a quantidade de fitas: "))
aluguel = float(input("Digite o valor do aluguel: "))
fatAnual = qtd/3 * aluguel * 12
multas = aluguel * 0.1 * (qtd/3)/10
print(f"Multas mensais: {multas:.3f}")
qtdFinal = qtd - qtd * 0.02 + qtd/10
print(f"Quantidade de fitas no final do ano: {qtdFinal:.3f}")
