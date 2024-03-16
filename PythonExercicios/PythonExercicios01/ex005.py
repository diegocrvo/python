# Faça um programa que leia um número inteiro e
# mostre na tela o seu sucessor e seu antecessor.
ni = int(input("Digite um número: "))
print(f"Analisando o número \033[32;1m{ni}\033[m, seu antecessor"
      f"\n é \033[31;1m{ni - 1}\033[m e o sucessor é \033[34;1m{ni + 1}\033[m.")
