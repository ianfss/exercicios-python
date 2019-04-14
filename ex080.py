# Exercício 080 - Lista ordenada sem repetições
numberList = []
count = 0
while True:
    if count == 5:
        break
    number = int(input('Digite um valor: '))

    if number in numberList:
        print('Número repetido!')

    if count == 0:
        numberList.append(number)
        print('O valor foi adicionado ao final da lista...')
        count += 1

    if count == 1:
        if number < numberList[0]:
            numberList.insert(0, number)
            print('O valor foi adicionado na posição 0...')
            count += 1
        if number > numberList[0]:
            numberList.append(number)
            print('O valor foi adicionado ao final da lista...')
            count += 1

    if count == 2:
        if number < numberList[0]:
            numberList.insert(0, number)
            print('O valor foi adicionado na posição 0...')
            count += 1
        if number > numberList[0] and number < numberList[1]:
            numberList.insert(1, number)
            print('O valor foi adicionado na posição 1...')
            count += 1
        if number > numberList[1]:
            numberList.append(number)
            print('O valor foi adicionado ao final da lista...')
            count += 1

    if count == 3:
        if number < numberList[0]:
            numberList.insert(0, number)
            print('O valor foi adicionado na posição 0...')
            count += 1
        if number > numberList[0] and number < numberList[1]:
            numberList.insert(1, number)
            print('O valor foi adicionado na posição 1...')
            count += 1
        if number > numberList[1] and number < numberList[2]:
            numberList.insert(2, number)
            print('O valor foi adicionado na posição 2...')
            count += 1
        if number > numberList[2]:
            numberList.append(number)
            print('O valor foi adicionado ao final da lista...')
            count += 1

    if count == 4:
        if number < numberList[0]:
            numberList.insert(0, number)
            print('O valor foi adicionado na posição 0...')
            count += 1
        if number > numberList[0] and number < numberList[1]:
            numberList.insert(1, number)
            print('O valor foi adicionado na posição 1...')
            count += 1
        if number > numberList[1] and number < numberList[2]:
            numberList.insert(2, number)
            print('O valor foi adicionado na posição 2...')
            count += 1
        if number > numberList[2] and number < numberList[3]:
            numberList.insert(3, number)
            print('O valor foi adicionado na posição 3...')
            count += 1
        if number > numberList[3]:
            numberList.append(number)
            print('O valor foi adicionado ao final da lista...')
            count += 1

print(f'Os valores digitados em ordem foram {numberList}')
