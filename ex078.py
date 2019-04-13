# Exercício 078 - Maior e Menor valores na Lista
numberList = []
for numberPosition in range(0, 5):
    numberList.append(int(input(f'Digite um valor para a Posição {numberPosition}: ')))
print(f'Você digitou os valores {numberList}')
print(f'O maior valor digitado foi {max(numberList)} nas posições ', end='')
for numberPosition, numberValue in enumerate(numberList):
    if max(numberList) == numberValue:
        print(f'{numberPosition}... ', end='')
print(f'\nO menor valor digitado foi {min(numberList)} nas posições ', end='')
for numberPosition, numberValue in enumerate(numberList):
    if min(numberList) == numberValue:
        print(f'{numberPosition}... ', end='')
print('\nAcabou!')
