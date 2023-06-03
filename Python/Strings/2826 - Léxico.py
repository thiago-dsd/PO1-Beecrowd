letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
p1 = input()
p2 = input()
marc = False
if len(p2) >= len(p1):
    for i in range(0, len(p1)):
        if letras.index(p1[i]) < letras.index(p2[i]):
            print(p1)
            print(p2)
            marc = True
            break
        if letras.index(p1[i]) > letras.index(p2[i]):
            print(p2)
            print(p1)
            marc = True
            break
    if marc == False:
        print(p1)
        print(p2)
else:
    for i in range(0, len(p2)):
        if letras.index(p1[i]) < letras.index(p2[i]):
            print(p1)
            print(p2)
            marc = True
            break
        if letras.index(p1[i]) > letras.index(p2[i]):
            print(p2)
            print(p1)
            marc = True
            break
    if marc == False:
        print(p2)
        print(p1)
    


