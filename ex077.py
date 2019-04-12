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
        print(f'\nNa palavra {words} temos ', end='')
        for vogals in words:
                if vogals in 'AEIOU':
                        print(vogals.lower(), end=' ')

