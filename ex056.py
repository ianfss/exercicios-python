# Exercício 056
idades = 0
mulheres = 0
homens = 0
velho = 0
for pessoa in range(1, 5):
    print(f'{pessoa}ª PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idades += idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M' and idade > homens:
        homens = idade
    if homens == idade:
        velho = nome
print(f'A média de idade do grupo é {idades / 4:.1f} anos.')
print(f'O número de mulheres com menos de 20 anos é {mulheres}.')
print(f'A idade do homem mais velho é {homens} anos e seu nome é {velho}')
