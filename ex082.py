# Exercício Python #082 - Dividindo valores em várias listas
numberList = []
evenList = []
oddList = []
while True:
    number = int(input('Digite um número: '))
    numberList.append(number)
    if number % 2 == 0:
        evenList.append(number)
    else:
        oddList.append(number)
    option = str(input('Quer continuar? [S/N] '))
    if option in 'Nn':
        break
print(f'A lista completa é {numberList}')
print(f'A lista de pares é {evenList}')
print(f'A lista de ímpares é {oddList}')
