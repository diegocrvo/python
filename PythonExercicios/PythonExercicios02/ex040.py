"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, conforme a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
----------------------------------------------------------------------------------"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Com as notas {nota1} e {nota2}, sua média total é {media}.'
      f'\nCom essa média o aluno está:')

if media < 5:
    print('\033[31mREPROVADO')

elif 5 <= media < 7:
    print('\033[33mEM RECUPERAÇÃO')

else:
    print('\033[32mAPROVADO')
