while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        for i in range(n):
            for j in range(n):
                if i == n-j-1:
                    print('2', end='')
                elif i == j:
                    print('1', end='')
                else:
                    print('3', end='')
            print()
