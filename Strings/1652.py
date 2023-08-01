n, l = map(int, input().split())

palavras = {}
for _ in range(n):
    key, value = input().split()
    palavras[key] = value
    
for _ in range(l):
    palavra = input()
    if palavra in palavras.keys():
        print(palavras[palavra])
    elif palavra[-1] == 'y' and palavra[-2] not in ('a', 'e', 'i', 'o', 'u'):
        print(palavra[:-1] + 'ies')
    elif palavra[-1] in ('o', 's', 'x') or palavra[-2:] in ('ch', 'sh'):
        print(palavra + 'es')
    else:
        print(palavra + 's')
