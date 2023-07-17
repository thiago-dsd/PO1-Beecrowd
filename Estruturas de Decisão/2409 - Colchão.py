ac, lc, cc = input().split()
ap, lp = input().split()
ac = int(ac)
lc = int(lc)
cc = int(cc)
ap = int(ap)
lp = int(lp)
#ac / lc
if ac <= ap and lc <= lp:
    print('S')
elif ac <= lp and lc <= ap:
    print('S')
else:
#ac / cc
    if ac <= ap and cc <= lp:
        print('S')
    elif ac <= lp and cc <= ap:
        print('S')
    else:
#lc / cc
        if lc <= ap and cc <= lp:
            print('S')
        elif lc <= lp and cc <= ap:
            print('S')
        else:
            print('N')
    

