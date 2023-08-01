c = 1
while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        rep_nome = None
        rep_nota = 11
        
        for _ in range(n):
            nome, nota = input().split()
            nota = int(nota)
            
            if nota < rep_nota:
                rep_nome = nome
                rep_nota = nota
            elif nota == rep_nota and nome > rep_nome:
                rep_nome = nome
        
        print('Instancia', c)
        print(rep_nome)
        print()
        
        c += 1
