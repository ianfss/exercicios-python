# Exercício 068 - Jogo do Par ou Ímpar
from random import randint
contador = 0
print('Vamos jogar PAR ou ÍMPAR?')
while True:
    ncomputador = randint(1, 5)
    njogador = int(input('Diga um valor: '))
    if njogador < 1 or njogador > 5:
        while njogador < 1 or njogador > 5:
            print('Ops! Diga um valor entre 1 e 5.')
            njogador = int(input('Diga um valor: '))
    ojogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if ojogador not in 'PI':
        while ojogador not in 'PI':
            print('Ops! Use P para PAR ou I para ÍMPAR.')
            ojogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = njogador + ncomputador
    par = soma % 2
    if par == 0:
        parouimpar = 'PAR'
    else:
        parouimpar = 'ÍMPAR'
    print(f'Você jogou {njogador} e o computador {ncomputador}. Total de {soma} deu {parouimpar}!')
    if ojogador in 'P' and parouimpar in 'PAR':
        print('VOCẼ GANHOU!')
        contador += 1
    else:
        print('VOCẼ PERDEU!')
        break
print(f'GAME OVER! Você venceu {contador} vezes.')
