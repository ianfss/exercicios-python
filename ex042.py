# Exercício 042
a = float(input('Informe a medida do primeiro segmento de reta: '))
b = float(input('Informe a medida do segundo segmento de reta: '))
c = float(input('Informe a medida do terceio segmento de reta: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Você PODE formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Você não pode formar um triângulo com estes segmentos de reta!')
