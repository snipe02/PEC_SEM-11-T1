populacao_inicial = int(input())
ano = 1600
nasc = 0
morre = 0
populacao_original = populacao_inicial

while populacao_inicial >= (10/100)*populacao_original:
    morre = (6/100)* populacao_inicial
    nasc = (1/100)* populacao_inicial   

    populacao_inicial += nasc
    populacao_inicial -= morre

    print(f'{ano},{nasc:.0f},{morre:.0f},{populacao_inicial:.0f}')
    ano += 1
    
