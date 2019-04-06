# Exercício 045
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
player = int(input('Qual é a sua jogada? '))
print(f'Computador jogou {itens[cpu]}!')
print(f'Você jogou {itens[player]}!')
if cpu == player:
    print('EMPATE!')
elif cpu == 0 and player == 2:
    print('O COMPUTADOR GANHOU!')
elif cpu == 1 and player == 0:
    print('O COMPUTADOR GANHOU!')
elif cpu == 2 and player == 1:
    print('O COMPUTADOR GANHOU!')
else:
    print('VOCÊ GANHOU!')

'''from time import sleep
from random import choice
player = str(input('Pedra, papel ou tesoura? ')).strip().lower()
sleep(1)
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!')
sleep(1)
list = ['pedra', 'papel', 'tesoura']
cpu = choice(list)
print(f'Você jogou {player} e o computador jogou {cpu}...')
if cpu == player:
    print('EMPATE!')
elif cpu == 'pedra' and player == 'tesoura':
    print('O COMPUTADOR GANHOU!')
elif cpu == 'papel' and player == 'pedra':
    print('O COMPUTADOR GANHOU!')
elif cpu == 'tesoura' and player == 'papel':
    print('O COMPUTADOR GANHOU!')
else:
    print('VOCÊ GANHOU!')'''