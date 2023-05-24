n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
med = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10
if med >= 7:
    print('Media: {:.1f}'.format(med))
    print('Aluno aprovado.')
else:
    if med < 5:
        print('Media: {:.1f}'.format(med))
        print('Aluno reprovado.')
    else:
        if 5 <= med <= 6.9:
            print('Media: {:.1f}'.format(med))
            print('Aluno em exame.')
            rec = float(input())
            nmed = ((rec + med)/2)
            nmed = float(nmed)
        if nmed >= 5:
            print('Nota do exame: {:.1f}'.format(rec))
            print('Aluno aprovado.')
            print('Media final: {:.1f}'.format(nmed))
        else:
            if nmed <= 4.9:
                print('Media: {:.1f}'.format(med))
                print('Aluno reprovado.')
        
    

