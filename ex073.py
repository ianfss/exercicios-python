# Exercício 073 - Tuplas com Times de Futebol
listaTimes = ('Atlético-PR', 'Atlético', 'Avaí', 'Bahia', 'Botafogo',
'CSA', 'Ceará SC', 'Chapecoense', 'Corinthians', 'Cruzeiro',
'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio',
'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco da Gama')
print('-=' * 20)
print(f'Lista de time do Brasileirão: {listaTimes}')
print('-=' * 20)
print(f'Os 5 primeiros são: {listaTimes[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {listaTimes[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(listaTimes)}')
print('-=' * 20)
print(f'O Chapecoense está na {listaTimes.index("Chapecoense")+1}ª posição')
# for posiçãoTime, nomeTime in enumerate(listaTimes, 1):
    # if nomeTime == 'Chapecoense':
        # print(f'O {nomeTime} está na {posiçãoTime}ª posição')
