num = input()
m = True
for x in range(0, len(num)-1):
    if num[x] == '1' and num[x+1] == '3':
        m = False
        print('{} es de Mala Suerte'.format(num))
        break
if m == True:
    print('{} NO es de Mala Suerte'.format(num))

