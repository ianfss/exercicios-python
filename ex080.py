# Exercício 080 - Lista ordenada sem repetições
numberList = list()
count = 0
while True:
    if count == 3:
        break
    number = int(input('Digite um valor: '))
    if count == 0:
        numberList.insert(0, number)
        count += 1
        print('Adcionado ao final da lista...')
    elif count == 1:
        if number > numberList[0]:
            numberList.insert(1, number)
            count += 1
            print('Adcionado ao final da lista...')
        else:
            numberList.insert(0, number)
            count += 1
            print('Adcionado na posição 0...')
    elif count == 2:
        if number > numberList[1]:
            numberList.insert(2, number)
            count += 1
            print('Adcionado ao final da lista...')
        elif number < numberList[1] and number > numberList[0]:
            numberList.insert(1, number)
            count += 1
            print('Adcionado na posição 1...')
        elif number < numberList[0]:
            numberList.insert(0, number)
            count += 1
            print('Adcionado na posição 0...')
print(numberList)
