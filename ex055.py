# Exercício 055
'''lista = []
for pesos in range(1, 6):
    peso = float(input(f'Peso da {pesos}ª pessoa: '))
    lista.append(peso)
print(f'O maior peso foi de {max(lista)}kg')
print(f'O menor peso foi de {min(lista)}kg')
'''
maior = 0
menor = 0
for pesos in range (1,6):
    peso = float(input(f'Peso da {pesos}ª pessoa: '))
    if pesos == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}kg')
print(f'O menor peso foi de {menor}kg')
