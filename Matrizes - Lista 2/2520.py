# desafio para mim: fazer o código se matrizes!

while True:
    try:
        n, m = [int(x) for x in input().split()]
    except EOFError:
        break
    else:
        for i in range(n):
            colunas = [int(x) for x in input().split()]
            for j in range(m):
                if colunas[j] == 2:
                    y_a = i
                    x_a = j
                if colunas[j] == 1:
                    y_j = i
                    x_j = j
        
        tot = 0
        if y_a >= y_j:
            tot += y_a - y_j
        else:
            tot += y_j - y_a
        
        if x_a >= x_j:
            tot += x_a - x_j
        else:
            tot += x_j - x_a
        
        print(tot)
