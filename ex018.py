# Exercício 018

from math import sin, cos, tan, radians
ang = float(input('Digite o ânulo que você deseja: '))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo de {ang}° tem o SENO de {sin:.2f}.')
print(f'O ângulo de {ang}° tem o COSSENO de {cos:.2f}.')
print(f'O ângulo de {ang}° tem a TANGENTE de {tan:.2f}.')
