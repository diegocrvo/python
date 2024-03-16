# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# -----------------------------------------------------------------------------

sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    print(f'O salário atualizado ficou: R${sal + (sal * 10 / 100):.2f}')
else:
    print(f'O salário atualizado ficou: R${sal + (sal * 15 / 100):.2f}')
