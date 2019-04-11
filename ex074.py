# Exercício 074 - Maior e menor valores em Tupla
from random import randint
randNumbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram:', end=' ')
for valueNumbers in randNumbers:
    print(f'{valueNumbers}', end=' ')
print(f'\nO maior número foi {max(randNumbers)}')
print(f'O menor número foi {min(randNumbers)}')
