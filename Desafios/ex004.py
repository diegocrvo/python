def processar_notas(lista_de_notas):
    for i, valor in enumerate(lista_de_notas):
        if valor >= 38 and (valor + 2) % 5 == 0:
            lista_de_notas[i] = valor + 2

lista = [73, 67, 38, 33]
processar_notas(lista)
print(lista)
