p = input()
ma_sorte = False
for i in range(len(p)-1):
    if p[i] == '1' and p[i+1] == '3':
        ma_sorte = True
        break

if ma_sorte:
    print(p, 'es de Mala Suerte')
else:
    print(p, 'NO es de Mala Suerte')
