def mdc(a, b, c):
    vals = [a, b, c]
    vals.sort()
    c, b, a = vals
    
    while c != 0:
        a, b, c = c, b % c, a % c
    
    return a


def isPit(a, b, c):
    vals = [a, b, c]
    vals.sort()
    a, b, c = vals
    
    return a*a + b*b == c*c


while True:
    try:
        a, b, c = [int(x) for x in input().split()]
    except EOFError:
        break
    else:
        if isPit(a, b, c):
            if mdc(a, b, c) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')
