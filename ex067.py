# Exercício 067 - Tabuada v3.0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
print('Programa encerrado.')
