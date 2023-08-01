conversao = [
    'GQaku',   # 0
    'ISblv',   # 1
    'EOYcmw',  # 2
    'FPZdnx',  # 3
    'JTeoy',   # 4
    'DNXfpz',  # 5
    'AKUgq',   # 6
    'CMWhr',   # 7
    'BLVis',   # 8
    'HRjt'     # 9
    ]

n = int(input())
for _ in range(n):
    entrada = ''.join(input().split())  # eliminar espaços
    final = ''
    for i in entrada[:12]:  # ir até o 12º caractere
        for k, v in enumerate(conversao):
            if i in v:
                final += str(k)
                break

    print(final)
