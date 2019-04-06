# Exercício Python 058 - Jogo da Adivinhação v2.0
from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
número = randint(0, 10)
palpite = -1
tentativas = 0
while palpite != número:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if palpite > número:
        print('Menos... Tente mais uma vez.')
    if palpite < número:
        print('Mais... Tente mais uma vez.')
print(f'Acertou com {tentativas} tentativas. Parabéns!')
