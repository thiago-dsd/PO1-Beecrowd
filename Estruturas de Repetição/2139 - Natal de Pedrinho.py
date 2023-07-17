t = [31,29,31,30,31,30,31,31,30,31,30,31]

while 1:
    try:
        x = input()
        x = x.split(' ')

        dd = int(x[1])
        mm = int(x[0])
        tt = 0

        if dd == 25 and mm == 12:
            print('E natal!')
        elif dd == 24 and mm == 12:
            print('E vespera de natal!')
        elif dd > 25 and mm == 12:
            print('Ja passou!')
        else:
            for i in range(mm - 1, len(t)):
                tt += t[i]

            tt -= dd
            tt -= 6

            print('Faltam %d dias para o natal!' %tt)
    except:
        break
