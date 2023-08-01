p_braille = [
    '.***',  # 0
    '*...',  # 1
    '*.*.',  # 2
    '**..',  # 3
    '**.*',  # 4
    '*..*',  # 5
    '***.',  # 6
    '****',  # 7
    '*.**',  # 8
    '.**.',  # 9
    ]

p_num = {x: str(k) for x, k in zip(p_braille, range(0, 10))}

while True:
    qtd_digs = int(input())
    if qtd_digs == 0:
        break
    letra = input()
    if letra == 'S':
        num = input()
        tmp1 = tmp2 = tmp3 = ''
        for i in num:
            i = int(i)
            tmp1 += p_braille[i][:2] + ' '
            tmp2 += p_braille[i][2:] + ' '
            tmp3 += '..' + ' '
        print(tmp1.strip())
        print(tmp2.strip())
        print(tmp3.strip())
        
    else:
        tmp1 = input().split()
        tmp2 = input().split()
        input()
        tmp = ''
        for i in range(len(tmp1)):
            dig = tmp1[i] + tmp2[i]
            tmp += p_num[dig]
        print(tmp)
