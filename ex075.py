# Exercício 075 - Análise de dados em uma Tupla

numberOne = int(input('Digite um número: '))
numberTwo = int(input('Digite outro número: '))
numberThree = int(input('Digite mais um número: '))
numberFour = int(input('Digite o último número: '))
numbersList = (numberOne, numberTwo, numberThree, numberFour)
print(f'Você digitou os valores {numbersList}')
print(f'O valor 9 apareceu {numbersList.count(9)} vezes')
print(f'O valor 3 apareceu na {numbersList.index(3)+1}ª posição')
print('Os valores pares digitados foram:', end='') 
for evenNumbers in numbersList:
    if evenNumbers % 2 == 0:
        print(f' {evenNumbers}', end='')
