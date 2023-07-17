valor = input()
COD, QUA = valor.split()
QUA = int(QUA)
COD = int(COD)
V = 0
V = float(V)
if COD == 1:
    V = 4
    print('Total: R$ {:.2f}'.format(QUA*V))
elif COD == 2:
    V = 4.5
    print('Total: R$ {:.2f}'.format(QUA*V))
elif COD == 3:
    V = 5.0
    print('Total: R$ {:.2f}'.format(QUA*V))
elif COD == 4:
    V = 2.0
    print('Total: R$ {:.2f}'.format(QUA*V))
elif COD == 5:
    V = 1.5
    print('Total: R$ {:.2f}'.format(QUA*V))


