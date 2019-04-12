# Exercício 077 - Contando vogais em Tupla

wordList = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
for words in wordList:
        print(f'Na palavra {words} temos ', end='')
        for vogals in words:
                if 'A' in vogals:
                        print('a', end=' ')
                elif 'E' in vogals:
                        print('e', end=' ')
                elif 'I' in vogals:
                        print('i', end=' ')
                elif 'O' in vogals:
                        print('o', end=' ')
                elif 'U' in vogals:
                        print('u', end=' ')
        print('\n')
