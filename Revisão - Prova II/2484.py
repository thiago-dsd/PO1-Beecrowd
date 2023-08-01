# 21 -> 11 no fim

ja_foi_o_primeiro = False
while True:
    try:
        palavra = input()
    except EOFError:
        break
    else:
        for i in range(len(palavra), 0, -1):
            print(' '*(len(palavra)-i), end='')
            for j in range(i):
                if j < i-1:
                    print(f'{palavra[j]} ', end='')
                else:
                    print(f'{palavra[j]}', end='')
            print()
        print()
