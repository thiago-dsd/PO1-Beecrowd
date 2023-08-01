n = int(input())

part = {}
for i in range(n):
    nome, p1, p2, p3 = input().split()
    part[nome] = [p1, p2, p3]
    
while True:
    try:
        nome, chute = input().split()
    except EOFError:
        break
    else:
        if chute in part.get(nome, []):
            print('Uhul! Seu amigo secreto vai adorar o/')
        else:
            print('Tente Novamente!')
