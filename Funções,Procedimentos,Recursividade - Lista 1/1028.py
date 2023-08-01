def mdc(a, b):
    a, b = max([a, b]), min([a, b])
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    _mdc = mdc(a, b)
    print(_mdc)
