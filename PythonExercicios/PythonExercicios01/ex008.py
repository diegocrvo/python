# Escreva um programa que leia um valor em
# metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite o total em metros: '))
print(f"Quantidade total em Quilômetros: \033[41;1m{m / 1000}km\033[m"
      f"\nToral em hectômetros: \033[42;1m{m / 100}hm\033[m"
      f"\nTotal em decâmetros: \033[43;1m{m / 10}dam\033[m"
      f"\nTotal em decímetros: \033[44;1m{m * 10:.0f}dm\033[m"
      f"\nTotal em centímetros: \033[45;1m{m * 100:.0f}cm\033[m"
      f"\nTotal em milímetros: \033[46;1m{m * 1000:.0f}mm\033[m")
