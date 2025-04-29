primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = 0

while (segundoValor <= primeiroValor):
    segundoValor = int(input("Digite o segundo valor: "))

total = 0
for i in range(primeiroValor, segundoValor + 1):
    total += i

print(f"A soma dos valores inteiros entre os informados, incluindo os mesmos, é: {total}")
