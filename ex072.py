# Exercício 072 - Número por Extenso
número = int(input('Digite um número entre 0 e 20: '))
while número < 0 or número > 20:
    número = int(input('Tente novamente. Digite um número entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {extenso[número]}.')
