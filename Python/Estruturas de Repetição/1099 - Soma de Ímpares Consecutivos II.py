teste = int(input())
for c in range (0, teste):
    somador = 0
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X > Y:
        #X É PAR
        if X % 2 == 0:
            for w in range (X-1, Y, -2):
                somador+= w
            print(somador)
        else:
            for z in range (X-2, Y, -2):
                somador += z
            print(somador)
    # Y > X
    else:
        if Y % 2 == 0:
            for w in range (Y-1, X, -2):
                somador+= w
            print(somador)
        else:
            for z in range (Y-2, X, -2):
                somador += z
            print(somador)
        

