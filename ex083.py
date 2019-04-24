# Exercício Python #083 - Validando expressões matemáticas
lista = []
expressao = str(input('Digite a expressão: '))
for parenteses in expressao:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print ('Sua expressão está válida!')
else:
    print ('Sua expressão está errada!')
