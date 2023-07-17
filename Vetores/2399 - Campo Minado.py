lista = []
num = int(input())
for c in range (0, num):
    teste = int(input())
    lista.append(teste)
if num == 1:
    if lista[0] == 1:
        print(1)
    else:
        print(0)
else:
    for i in range (0, num):
        bombas = 0
        if i == (num - 1):
            if lista[i] == 1:
                bombas += 1
            if lista[i-1] == 1:
                bombas += 1
        elif i == 0:
            if lista[i] == 1:
                bombas += 1
            if lista[i+1] == 1:
                bombas += 1  
        else:   
            if lista[i] == 1:
                bombas += 1
                if lista[i-1] == 1:
                    bombas += 1
                if lista[i+1] == 1:
                    bombas += 1
            else:
                if lista[i-1] == 1:
                    bombas += 1
                if lista[i+1] == 1:
                    bombas += 1
        print(bombas)
    


