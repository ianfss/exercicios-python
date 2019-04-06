# Exercício 036
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = float(input('Em quantos anos você deseja pagar? '))
parcela = casa / (tempo * 12)
credito = 30 * salario / 100
if credito <= parcela:
    print(f'Você não pode comprar a casa em {tempo * 12:.0f} parcelas.')
elif credito >= parcela:
    print(f'Parabéns! Você pode comprar a casa em {tempo * 2:.0f} parcelas no valor de R${parcela:.2f} mensais.')
print('Obrigado por utilizar nossos serviços.')
