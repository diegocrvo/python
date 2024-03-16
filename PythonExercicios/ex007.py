# Desenvolva um programa que leia as duas notas
# de um aluno, calcule e mostre a sua média.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
# Para apenas 1 digito após a vírgula ex.: {(n1+n2)/2:.1f}
m = (n1 + n2) / 2
if m <= 5:
    print(f'A média do aluno é: \033[31;1m{m}\033[m')
if m > 5:
    print(f'A média do aluno é: \033[32;1m{m}\033[m')
