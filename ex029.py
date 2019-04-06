# Exercício 029
vel = int(input('Qual a velocidade que o carro estava? '))
vmulta = 7
velmax = 80
multa = (vel - velmax) * vmulta
if vel > velmax:
    print(f'Você ultrapassou o limite de {velmax}km/h. A sua multa é de {multa} reais.')
