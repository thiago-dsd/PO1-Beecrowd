cv, ce, cs, fv, fe, fs = input().split()
cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)
pC = cv*3 + ce*1
pF = fv*3 + fe*1
if pC == pF:
    if cs > fs:
        print('C')
    elif fs > cs:
        print('F')
    else:
        print('=')
else:
    if pC > pF:
        print('C')
    else:
        print('F')

