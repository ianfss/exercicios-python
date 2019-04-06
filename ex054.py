# Exercício 054
from datetime import date
tmaior = 0
tmenor = 0
for anos in range(1, 8):
    ano = int(input(f'Em que ano a {anos}ª pessoa nasceu? '))
    if date.today().year - ano >= 21:
        tmaior += 1
    else:
        tmenor += 1
print(f'Ao todo tivemos {tmaior} pessoas MAIORES de idade.')
print(f'E também tivemos {tmenor} pessoas MENORES de idade.')
