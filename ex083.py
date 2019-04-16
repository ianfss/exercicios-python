# Exercício Python #083 - Validando expressões matemáticas
expressao = str(input('Digite a expressão: '))
abre = (expressao.count("("))
fecha = (expressao.count(")"))
if abre == fecha:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')

# (a+b)*c
