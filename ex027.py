# Exercício 027
nome = str(input('Digite seu nome completo: ')).strip()
first = nome.split()[0]
last = nome.split()[-1]
print(f'Seu primeiro nome é {first}\nSeu último nome é {last}')
