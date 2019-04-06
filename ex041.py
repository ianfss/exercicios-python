# Exercício 041
from datetime import date
ano = int(input('Informe o ano de seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na categoria INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na categoria JUNIOR!')
elif idade <= 20:
    print(f'Você tem {idade} anos e está na categoria SÊNIOR!')
else:
    print(f'Você tem {idade} anos e está categoria MASTER!')
print('Boa sorte!')