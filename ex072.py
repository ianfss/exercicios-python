# Exercício 072 - Número por Extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if número < 0 or número > 20:
        print('Tente novamente. ', end='')
    elif 0 <= número <= 20:
        print(f'Você digitou o número {extenso[número]}.')
        continuar = str(input('Você quer continuar? [S/N] ')).strip()[0]
        if continuar in ('nN'):
            break
