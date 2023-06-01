t, o, l = input().split()
t = int(t)
o = int(o)
l = int(l)
PT = t // 2
PO = o // 3
PL = l // 5
if PT <= PO and PT <= PL:
    print(PT)
elif PO <= PT and PO <= PL:
    print(PO)
else:
    print(PL)

