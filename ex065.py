# Exercício 065 - Maior e Menor valores

soma = total = maior = menor = 0
opção = 'S'
while opção in 'Ss':
    número = int(input('Digite um número: '))
    opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += número
    total += 1
    if total == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        elif número < menor:
            menor = número
média = soma / total
print(f'Você digitou {total} números e a média foi {média:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
