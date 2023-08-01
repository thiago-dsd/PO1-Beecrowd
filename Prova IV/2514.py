from math import lcm

while True:
    try:
        m = int(input())
    except EOFError:
        break
    else:
        l1, l2, l3 = [int(x) for x in input().split()]
        daqui = lcm(l1, l2, l3)
        X = daqui - m
        print(X)
