# Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então o empréstimo será negado.
# ----------------------------------------------------------------------------------
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do cliente? '))
anos = int(input('Em quantos anos deseja pagar? '))
porcentagem_salario = salario * 0.3
prestacao = casa / anos / 12
print(f'Para pagar uma casa no valor de R${casa:.2f} em {anos} anos, o valor mensal será de '
      f'\nR${prestacao:.2f}')
if prestacao > porcentagem_salario:
    print('\033[31mInfelizmente o empréstimo não foi aprovado!\033[m'
          '\nO valor da parcela excede 30% do salário do comprador.')
else:
    print('\033[32mParabéns, empréstimo aprovado com sucesso!')
