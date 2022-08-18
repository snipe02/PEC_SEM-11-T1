ano = 0
populacao_A = int(input())
populacao_B = int(input())
populacao_maior = 0
populacao_menor = 0


if populacao_B > populacao_A:
    populacao_maior = populacao_B
    populacao_menor = populacao_A
else:
    populacao_maior = populacao_A
    populacao_menor = populacao_B


while populacao_maior > populacao_menor:
    populacao_menor += 0.03 * populacao_menor
    populacao_maior += 2/100 * populacao_maior
    ano += 1

print(f'{ano}')
