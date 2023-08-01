# Linha: competidor, Coluna: questao
# 1: ha 0 em todas as linhas
# 2: ha 1 em todas as colunas
# 3: ha 0 em todas as colunas
# 4: ha 1 em todas as linhas

while True:
    n, m = [int(x) for x in input().split()]
    
    if n == 0:
        break
    
    mat = []
    carac = 0
    ha_um1 = ha_um2 = ha_zero1 = ha_zero2 = True
    for _ in range(n):
        entrada = [int(x) for x in input().split()]
        if not (1 in entrada):
            ha_um1 = False
        if not (0 in entrada):
            ha_zero1 = False
        mat.append(entrada)
    
    for j in range(m):
        tmp_ha_um2 = tmp_ha_zero2 = False
        for i in range(n):
            if mat[i][j] == 0:
                tmp_ha_zero2 = True
            if mat[i][j] == 1:
                tmp_ha_um2 = True
        if not tmp_ha_zero2:
            ha_zero2 = False
        if not tmp_ha_um2:
            ha_um2 = False
            
    if ha_um1:
        carac += 1
    if ha_zero1:
        carac += 1
    if ha_um2:
        carac += 1
    if ha_zero2:
        carac += 1
        
    print(carac)
