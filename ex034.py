# Exercício 034
'''salario = int(input('Qual é o seu salário? '))
dez = salario * 10 /100
quinze = salario * 15 / 100
if salario <= 1250:
    print(f'Você recebeu um aumento de 15% no valor de {quinze:.2f} reais. Seu novo salário é {quinze + salario:.2f} reais!')
else:
    print(f'Você recebeu um aumento de 10% no valor de {dez:.2f} reais. Seu novo salário é {dez + salario:.2f} reais!')'''

salario = int(input('Qual é o salário do funcionário? '))
if salario <= 1250:
    nsalario = salario (salario * 15 / 100)
else:
    nsalario = salario + (salario * 10 / 100)
print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {nsalario:.2f} agora.')
