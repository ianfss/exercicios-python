# Exercício 025
nome = str(input('Qual é o seu nome completo? ')).strip()
check = 'Silva' in nome.title()
print(f'Seu nome tem Silva? {check}.')
