# Exercício 031
dist = int(input('Qual a distância da sua viagem? '))
viag1 = 0.50 * dist
viag2 = 0.45 * dist
if dist <= 200:
    print(f'O valor da sua passagem é {viag1} reais.')
else:
    print(f'O valor da sua passagem é {viag2} reais.')
print('Obrigado por viajar conosco. Boa viagem!')
