# Exercício 012

preco = float(input('Qual o valor do produto? '))
desconto = 5
novopreco = preco-((desconto*preco)/100)
print(f'O produto com o valor de {preco:.2f} sai por {novopreco:.2f} com 5% de desconto!')

# Uma outra possibilidade é já colocar o desconto em forma de porcentagem que pode ser usada diretamente no cálculo.
# 5% é o mesmo que 5/100 = 0.05
# Então o código pode ficar assim:
# 
# desconto = 0.05
# novopreco = preco - (desconto * preco)
# 
# com o restante igual
