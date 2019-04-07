# Exercício 015

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (60.0 * dias) + (0.15 * km)
print(f'O total a pagar é de R${pago}')
