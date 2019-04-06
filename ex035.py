# Exercício 035
a = float(input('Informe a medida do primeiro segmento de reta: '))
b = float(input('Informe a medida do segundo segmento de reta: '))
c = float(input('Informe a medida do terceio segmento de reta: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Você pode formar um triângulo com estes segmentos de reta!')
else:
    print('Você não pode formar um triângulo com estes segmentos de reta!')
