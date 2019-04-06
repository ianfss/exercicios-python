# Exercício 024

cidadea = str(input('Em que cidade você nasceu? ')).split()
cidadeb = 'Santo'
resultado = cidadeb in cidadea[0].capitalize()
if resultado == True:
    print(f'Sua cidade começa com {cidadea[0].capitalize()}.')
else:
    print(f'Sua cidade não começa com {cidadeb}.')
