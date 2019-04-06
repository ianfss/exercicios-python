# Exercício 053
frase = str(input('Digite uma frase: ')).upper().split()
frase = ''.join(frase)
esarf = ''.join(frase[::-1])
print(f'O inverso de {frase} é {esarf}') 
if frase == esarf:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídromo!')

'''frase = str(input('Digite uma frase: ')).upper().split()
junto = ''.join(frase)
otnuj = ''
for a in range(len(junto) -1, -1, -1):
    otnuj += junto[a]
print(f'O inverso de {junto} é {otnuj}') 
if junto == otnuj:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídromo!')'''
