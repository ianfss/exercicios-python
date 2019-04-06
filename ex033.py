# Exercício 033
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
if num1 < num2 and num1 < num3:
    print(f'{num1} é o MENOR número!')
if num2 < num1 and num2 < num3:
    print(f'{num2} é o MENOR número!')
if num3 < num1 and num3 < num2:
    print(f'{num3} é o MENOR número!')
if num1 > num2 and num1 > num3:
    print(f'{num1} é o MAIOR número!')
if num2 > num1 and num2 > num3:
    print(f'{num2} é o MAIOR número!')
if num3 > num1 and num3 > num2:
    print(f'{num3} é o MAIOR número!')
