# Exercício 044
prod = float(input('Valor do produto: '))
dinche = prod - (10 * prod / 100)
carvis = prod - (5 * prod / 100)
cartre = prod + (20 *prod / 100)
cond = int(input('Digite 0 para dinheiro ou cheque e 1 para cartão: '))
if cond == 0:
    print(f'O seu produto custará R${dinche:.2f} à vista no dinheiro ou cheque.')
elif cond == 1:
    parc = int(input('Informe em quantas vezes você deseja dividir ou 1 para à vista: '))
    if parc == 1:
        print(f'O seu produto custará R${carvis:.2f}.')
    elif parc == 2:
        print(f'O seu produto custará R${prod:.2f}.')
    elif parc >= 3:
        print(f'O seu produto custará R${cartre:.2f}.')
print('Obrigado e volte sempre!')
