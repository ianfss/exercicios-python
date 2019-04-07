# Exercício 064 - Tratando vários valores v1.0

soma = total = número = 0
while número != 999:
    número = int(input('Digite um número [999 para parar]: '))
    if número != 999:
        soma += número
        total += 1
print(f'Você digitou {total} números e a soma entre eles foi {soma}')
