# Exercício 079 - Valore únicos em uma lista

uniqueList = []
while True:
    number = int(input('Digite um valor: '))

    if number in uniqueList:
        print('Valor duplicado! Não vou adicionar...')
    elif number not in uniqueList:
        uniqueList.append(number)
        print('Valor adicionado com sucesso...')

    continueOption = str(input('Você quer continuar? [S/N] ')).strip()[0]
    if continueOption in 'Nn':
        break
        
uniqueList.sort()
print(f'Você digitou os valores {uniqueList}')
