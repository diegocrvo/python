# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por km rodado.
# --------------------------------------------------------------------------
km = float(input('Qual a quantidade de km percorrido?: '))
dias = int(input('Quantos dias alugado?: '))
print(f'Valor total a pagar: R${(60 * dias) + (km * 0.15):.2f}')
