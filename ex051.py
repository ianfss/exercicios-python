# Exercício 051
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for pa in range(termo, decimo + razao, razao):
    print(pa, end=' → ')
print('ACABOU')
