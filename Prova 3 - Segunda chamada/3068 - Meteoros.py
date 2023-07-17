contador = 1
while True:
    entrada = input()
    if entrada == "0 0 0 0":
        break
    X1, Y1, X2, Y2 = entrada.split()
    X1, Y1, X2, Y2 = int(X1), int(Y1), int(X2),int(Y2)
    num = int(input())
    numMeteoritos = 0
    for _ in range (num):
        numMeteoritos += 1
        X, Y = input().split()
        X, Y = int(X), int(Y)
        if X > X2 or X < X1 or Y > Y1 or Y < Y2:
            numMeteoritos -= 1
    print("Teste {}".format(contador))
    print(numMeteoritos)
    contador += 1
            
        

