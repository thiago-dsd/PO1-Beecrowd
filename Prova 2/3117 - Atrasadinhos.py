qntAlunos, qntMin = input().split()
qntAlunos, qntMin = int(qntAlunos), int(qntMin)
entrada = input().split()
atrasados = 0
for v in range (0, len(entrada)):
    entrada[v] = int(entrada[v])
    if entrada[v] > 0:
        atrasados += 1
pontual = qntAlunos - atrasados
if pontual >= qntMin:
    print('YES')
else:
    print('NO')

