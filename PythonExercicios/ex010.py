# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere USS1.00 = RS3.27
s = float(input('Quanto você tem na carteira? R$'))
print(f'Com \033[33mR${s}\033[m você compra \033[32mUS${s / 4.94:.2f}\033[m'
      f' ou \033[36mEUR{s / 5.39:.2f}\033[m.')
