# Exercício 069 - Análise de dados do grupo
tmaiores = thomens = tmulheres = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        tmaiores += 1
    if sexo in 'M':
        thomens += 1
    if sexo in 'F' and idade < 20:
        tmulheres += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'Total de pessoas com 18 ou mais: {tmaiores}')
print(f'Total de homens cadastrados: {thomens}')
print(f'Total de mulheres com menos de 20 anos: {tmulheres}')
