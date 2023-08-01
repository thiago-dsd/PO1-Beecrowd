def r(x, y):
    return 9*x**2 + y**2

def b(x, y):
    return 2*x**2 + 25*y**2

def c(x, y):
    return -100*x + y**3

n = int(input())
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    _r = r(x, y)
    _b = b(x, y)
    _c = c(x, y)
    
    maior = max([_r, _b, _c])
    if maior == _r:
        print('Rafael ganhou')
    elif maior == _b:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')
