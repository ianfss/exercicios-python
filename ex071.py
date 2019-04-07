# Exercício 071 - Simulador de Caixa Eletrônico
valor = int(input('Quanto você quer sacar? '))
tvalor = valor
cedula = 100
tcedula = 0
while True:
    if tvalor >= cedula:
        tvalor -= cedula
        tcedula += 1
    else:
        if tcedula > 0:
            print(f'{tcedula} cédulas de {cedula:.2f}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        tcedula = 0
        if tvalor == 0:
            break
print('Volte sempre!')
