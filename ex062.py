# Exercício 062 - Super Progressão Aritmética v3.0 
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
mais = 10
total = 0
while mais != 0:
    contador = 0
    while contador < mais:
        print(f'{termo} → ', end='')
        termo += razão
        contador += 1
        total += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
