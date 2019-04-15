# Exercício Python #081 - Extraindo dados de uma Lista
numberList = list()
numberCount = 0
while True:
    numberList.append(int(input('Digite um valor: ')))
    option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if option in 'Nn':
        break
print(f'Você digitou {len(numberList)} elementos.')
# numberList.sort(reverse = True)
print(f'Os valores em ordem decrescente são {sorted(numberList, reverse=True)}')
if 5 in numberList:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
