# Exercício 028
from random import randint
num = int(input('Pensei em um número entre 0 e 5... Você consegue advinhar qual? '))
rnum = randint(0, 5)
if num == rnum:
    print('Parabéns, você acertou!')
else:
    print('Desculpe, eu venci.')
print(f'O número era {rnum}.')
