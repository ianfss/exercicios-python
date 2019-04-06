# Exercício 040
n1 = float(input('Informe a sua primeira nota: '))
n2 = float(input('Informe a sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Você foi REPROVADO!')
elif 5 <= m < 7:
    print('Você está em RECUPERAÇÃO!')
else:
    print('Parabéns! Você foi APROVADO!')
print('Bons estudos!')
