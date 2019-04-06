# Exercício 026
frase = str(input('Digite uma frase: ')).strip()
x = frase.upper().count('A')
p = frase.upper().find('A')+1
u = frase.upper().rfind('A')+1
print(f'A letra A aparece {x} vezes na frase.')
print(f'A primeira letra A apareceu na posição {p}.')
print(f'A última letra A apareceu na posição {u}.')
