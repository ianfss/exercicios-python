# Exercício 022
nome = str(input('Digite o seu nome completo: ')).strip()
dividido = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome)-nome.count(" ")} letras')
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras.')
