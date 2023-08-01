while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        ep = eh = intr = 0
        for _ in range(n):
            _, curso = input().split()
            if curso == 'EPR':
                ep += 1
            elif curso == 'EHD':
                eh += 1
            else:
                intr += 1
        print('EPR:', ep)
        print('EHD:', eh)
        print('INTRUSOS:', intr)
