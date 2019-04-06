# Exercício 052
num = int(input('Digite um número: ')) # recebe o valor digitado
x = 0 # reseta o contador para 0
for pri in range(1, num+1): # define o loop de 1 para o numero digitado + 1
    if num % pri == 0: # se o numero // numero do loop 
        print('(',end='') # coloca um parenteses antes do numero primo
        x += 1 # x + x = 1
        print(f'{pri})', end=' ') # coloca um parenteses depois do numero primo
    else:
        print(f'{pri}', end=' ') # escreve o resto dos numeros não primos
print(f'\nO número {num} foi divísivel {x} vezes')
if x == 2: # se o contador for igual a 2 o numero é primo (1 e ele mesmo)
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
