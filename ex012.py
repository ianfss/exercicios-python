# Exercício 012

preco = float(input('Qual o valor do produto? '))
desconto = 5
novopreco = preco-((desconto*preco)/100)
print(f'O produto com o valor de {preco:.2f} sai por {novopreco:.2f} com 5% de desconto!')
