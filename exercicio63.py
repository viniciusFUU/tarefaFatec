horasTrabalhadas=int(input("Digite as horas trabalhadas: "))
horaAula=int(input("Valor da hora-aula: "))
desconto=float(input("Digite o percentual de desconto: "))
sb = horasTrabalhadas * horaAula
td = (desconto / 100) * sb
sl = sb - td
print(f"Salário liquido: {sl}")