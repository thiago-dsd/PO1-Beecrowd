num = input()
CO, FO, FOPCO = num.split()
CO = int(CO)
FO = int(FO)
FOPCO = int(FOPCO)
if FO/(CO*FOPCO) >= 1:
    print('S')
else:
    print('N')

