# Exercício 070 - Estatísticas em produtos
print('LOJA SUPER BARATÃO')
vtotal = cmil = contador = 0
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preço = float(input('R$'))
    contador += 1
    vtotal += preço
    if preço >= 1000:
        cmil += 1
    if contador == 1:
        vbarato = preço
        pbarato = produto
    else:
        if preço < vbarato:
            vbarato = preço
            pbarato = produto
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${vtotal:.2f}')
print(f'Temos {cmil} produtos custando R$1000.00 ou mais')
print(f'O produto mais barato foi {pbarato} que custa R${vbarato:.2f}')
