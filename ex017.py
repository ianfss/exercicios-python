# Exercício 017

from math import hypot
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))
hypot = hypot(catop, catad)
print(f'A hipotenusa vai medir {hypot:.2f}')
