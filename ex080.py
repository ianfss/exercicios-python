# Exercício 080 - Lista ordenada sem repetições
numberList = []
for count in range(0, 5):
    number = int(input('Digite um valor: '))
    if count == 0 or number > numberList[len(numberList)-1]:
        numberList.append(number)
        print('Valor adicionado no final da lista...')
    else:
        position = 0
        while position < len(numberList):
            if number <= numberList[position]:
                numberList.insert(position, number)
                print(f'Valor adicionado na posição {position} da lista...')
                break
            position += 1
print(f'Os valores digitados foram {numberList}')
