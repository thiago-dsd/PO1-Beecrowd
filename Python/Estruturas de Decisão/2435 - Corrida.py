na , da, va = input().split()
nb , db, vb = input().split()
na = int(na)
nb = int(nb)
da = int(da)
va = int(va)
db = int(db)
vb = int(vb)
ta = da/va
tb = db/vb
if ta < tb:
    print(na)
else:
    print(nb)
