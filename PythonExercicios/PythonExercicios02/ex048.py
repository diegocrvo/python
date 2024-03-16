"""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
-------------------------------------------------------------------------------------"""
total = 0
saldo = 0
for n in range(1, 501, 2):

    if n % 3 == 0:
        total += n
        saldo += 1

print(f'A soma total dos {saldo} valores solicitados é de {total}.')
