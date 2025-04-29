contador = 0
lista = []

while (contador < 50):
    valor = int(input(f"Digite o {contador + 1}º número: "))
    lista.append(valor)
    contador += 1

eventos = {}
for indice, valor in enumerate(lista):
    if valor in eventos:
        eventos[valor].append(indice)
    else:
        eventos[valor] = [indice]

repetidos = {valor: indices for valor, indices in eventos.items() if len(indices) > 1}

for valor, indices in repetidos.items():
    print(f"Valor {valor} se repete nos índices: {indices}")
