# Exercício 039
from datetime import date
ano = int(input('Qual o ano de seu nascimento, jovem? '))
anoatual = date.today().year
idade = anoatual - ano
atrasado = idade - 18
faltam = 18 - idade
if idade == 18:
    print('Você precisa se alistar este ano!')
elif idade > 18:
    print(f'Você deveria ter se alistado {atrasado} anos atrás!')
elif idade < 18:
    print(f'Você só precisa se alistar daqui a {faltam} anos!')
