# Exerício 060 - Cálculo do Fatorial

# Usando while
número = int(input('Digite um número para calcular seu fatorial: '))
contador = número
fatorial = 1
print(f'Calculando {número}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    if contador > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')

# Usando for
número = int(input('Digite um número para calcular seu fatorial: '))
contador = número
fatorial = 1
print(f'Calculando {número}! = ', end='')
for contador in range(número, 0, -1):
    print(f'{contador}', end='')
    if contador > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= contador
print(f'{fatorial}')
