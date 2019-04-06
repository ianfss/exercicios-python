# Exercício 032
ano = int(input('Informe um ano: '))
bi1 = ano % 4
bi2 = ano % 100
bi3 = ano % 400
if bi1 == 0 and bi2 != 0 or bi3 == 0:
    print(f'{ano} é bissexto!')
else:
    print(f'{ano} NÃO é bissexto!')
