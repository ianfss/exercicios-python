# Exercício 075 - Análise de dados em uma Tupla

numbersList = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print(f'Você digitou os valores {numbersList}')
print(f'O valor 9 apareceu {numbersList.count(9)} vezes')
if 3 in numbersList:
    print(f'O valor 3 apareceu na {numbersList.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='') 
for evenNumbers in numbersList:
    if evenNumbers % 2 == 0:
        print(f'{evenNumbers}', end=' ')
