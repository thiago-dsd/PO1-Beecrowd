h, n = input().split()
h = int(h)
n = int(n)
lista = input().split()
for c in range (0, n):
    if c == n-1:
        print('YOU WIN')
        break
    else:
        lista[0] = int(lista[0])
        lista[1] = int(lista[1])
        if c == 0:
            if ((lista[0] - lista[1])**2)**0.5 <= h:
                ok = 1
            else:
                print('GAME OVER')
                break
        else:
            lista[c] = int(lista[c])
            lista[c+1] = int(lista[c+1])
            if ((lista[c] - lista[c+1])**2)**0.5 <= h:
                ok = 1
            else:
                print('GAME OVER')
                break
                


