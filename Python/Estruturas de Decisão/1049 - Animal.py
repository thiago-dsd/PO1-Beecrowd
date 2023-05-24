A = str(input())
B = str(input())
C = str(input())
if A == 'vertebrado':
    if B == 'ave':
        if C == 'carnivoro':
            print('aguia')
        if C == 'onivoro':
            print('pomba')              
    else:
        if C == 'onivoro':
            print('homem')
        if C == 'herbivoro':
            print('vaca')
else:
    if B == 'inseto':
        if C == 'hematofago':
            print('pulga')
        if C == 'herbivoro':
            print('lagarta')
    else:        
        if C == 'hematofago':
            print('sanguessuga')
        if C == 'onivoro':
            print('minhoca')

