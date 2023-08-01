while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        ordem = []
        for _ in range(n):
            cad = input()
            ordem.append(cad)
            
        ordem.sort()
        for cad in ordem:
            print(cad)
