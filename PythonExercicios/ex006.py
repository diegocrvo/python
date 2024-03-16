# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
print(f"O dobro de \033[32;1m{n}\033[m vale \033[31;1m{n*2}\033[m "
      f"\nO triplo vale \033[33;1m{n*3}\033[m "
      f"\nE a raiz quadrada é \033[34;4m{n**(1/2):.2f}\033[m")
