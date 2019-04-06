# Exercício 063 - Sequência de Fibonacci v1.0
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = t1 + t2
contador = 3
print(f'{t1} → {t2} → ', end='')
while contador < termos:
    t3 = t1 + t2
    print(f'{t3}', end='')
    print(' → ', end='')
    t1 = t2
    t2 = t3
    contador +=1
print('FIM')
