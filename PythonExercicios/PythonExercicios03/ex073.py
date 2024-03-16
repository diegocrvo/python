"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time Chapecoense.
--------------------------------------------------------------------------------------"""
tabela = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo',
          'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
          'Internacional', 'Chapecoense', 'Fortaleza', 'São Paulo', 'Cuiabá',
          'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia',
          'Santos', 'Goiás', 'Coritiba', 'América-MG')

print('\033[32m=-\033[m' * 160)
print('Lista de times do Campeonato Brasileiro de Futebol'.upper())
print('-' * 260)
print(tabela)
print('\033[32m=-\033[m' * 160)
print('PRIMEIROS 5 COLOCADOS')
print('-' * 260)
print(tabela[0:5])
print('\033[32m=-\033[m' * 160)
print('ÚLTIMOS 4 COLOCADOS')
print('-' * 260)
print(tabela[-4:])
print('\033[32m=-\033[m' * 160)
print('LISTA DOS TIMES DO BRASILEIRÃO EM ORDEM ALFABÉTICA')
print('-' * 260)
print(sorted(tabela))
print('\033[32m=-\033[m' * 160)
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição.')
