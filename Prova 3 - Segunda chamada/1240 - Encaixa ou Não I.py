n = int(input())
for _ in range (n):
    maior, menor = input().split()
    qntAlgMenor = len(menor)
    #print(qntAlgMenor)
    qntAlgMaior = len(maior)
    final = maior[(qntAlgMaior - qntAlgMenor):qntAlgMaior]
    #print(final)
    
    if len(maior) != len(menor):
        if menor == maior[(qntAlgMaior - qntAlgMenor):qntAlgMaior]:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        if menor == maior:
            print("encaixa")
        else:
            print("nao encaixa")


