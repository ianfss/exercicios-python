# Exercício 066 - Vários números com flag
soma = contador = 0
while True:
    número = int(input('Digite um valor [999 para parar]: '))
    if número == 999:
        break
    contador += 1
    soma += número
print(f'A soma dos {contador} valores foi {soma}!')
