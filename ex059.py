# Exercício Python 059 - Criando um Menu de Opções
from time import sleep
maior = 0
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma entre {primeiro} + {segundo} é {primeiro + segundo}')
    elif opção == 2:
        print(f'O resultado de {primeiro} x {segundo} é {primeiro * segundo}')
    elif opção == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print(f'Entre {primeiro} e {segundo} o maior valor é {maior}')
    elif opção == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(1)
print('Fim do programa')
