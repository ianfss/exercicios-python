# Exercício 048
s = 0
t = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        t += 1 # t = t + 1
        s += n # s = s + n
print(f'A soma de todos os {t} valores solicitados é {s}.')
