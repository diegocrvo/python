"""Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do
programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
------------------------------------------------------------------------------------"""
pessoas_cadastradas = 0
total_idade = 0
idade_maior = 0
nome_pessoa_velha = ''
quant_mulher_20menos = 0

for c in range(0, 4):
    nome = str(input('Digite o nome: ')).strip().title()
    idade = int(input('Digite a idade: '))
    print('''Qual o sexo?
    [ 1 ] - Masculino
    [ 2 ] - Feminino''')
    sexo = int(input('Digite 1 ou 2: '))
    print('-' * 40)

    pessoas_cadastradas += 1
    total_idade += idade

    if sexo == 1 and idade > idade_maior:
        idade_maior = idade
        nome_pessoa_velha = nome

    if sexo == 2 and idade < 20:
        quant_mulher_20menos += 1

media_idade = total_idade / pessoas_cadastradas

print(f'A média de idade do grupo é {media_idade:.2f} anos.')
print(f'O homem mais velho se chama {nome_pessoa_velha} e tem {idade_maior} anos.')
print(f'Existe(em) {quant_mulher_20menos} mulher(res) com menos de 20 anos.')
