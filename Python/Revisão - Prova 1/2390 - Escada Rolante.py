num = int(input())
economia = 0
anm1 = 0
an = 0
for c in range (1, num + 1):
        if c == 1:
            an = int(input())       
            anm1 = an
            economia = 0
        else:
            an = int(input())
            if an - anm1 <= 10:
                economia += -1*((an) - (anm1 + 10))
                anm1 = an
                an = 0
            else:
                anm1 = an
                an = 0
print(num*10 - economia)


