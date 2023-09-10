conta = int(input("Digite conta de três dígitos: "))
dl = conta // 100;
d2 = conta % 100 // 10;
d3 = conta % 100 % 10;
mv = d3 *100 + d2 *10 +dl;
soma = conta + mv;
dl = (soma // 100) * 1;
d2 = (soma % 100 // 10) * 2;
d3 = (soma % 100 % 10) *3;
digito = (dl +d2 +d3) % 10; 

print(f"Digito verificador: {digito}")
