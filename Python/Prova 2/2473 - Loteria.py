jogados = input().split()
sorteados = input().split()
qnt = 0
for n in range (0, 6):
    for l in range (0, 6):
        if jogados[n] == sorteados[l]:
            qnt += 1
if qnt == 3:
    print('terno')
elif qnt == 4:
    print('quadra')
elif qnt == 5:
    print('quina')
elif qnt == 6:
    print('sena')
else:
    print('azar')

