# Exercício 074 - Maior e menor valores em Tupla
from random import randint
randNumbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram:', end=' ')
for valueNumbers in randNumbers:
    print(f'{valueNumbers}', end=' ')
print('')
smallerNumber = biggerNumber = sorted(randNumbers)
print(f'O maior valor foi {smallerNumber[0]}')
print(f'O menor valor foi {biggerNumber[4]}')
