# Exercício 050
s = 0
t = 0
for c in range(0, 6):
    n = int(input('Informe um valor: '))
    if n % 2 == 0:
        t = t + 1 # t = t + 1
        s = s + n # s = s + n
print(f'A soma dos {t} valores PARES é {s}.')
