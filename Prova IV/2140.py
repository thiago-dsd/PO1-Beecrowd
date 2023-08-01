# 2, 5, 10, 20, 50, 100

while True:
    n, m = [int(x) for x in input().split()]
    
    if n + m == 0:
        break
    
    r = m - n # m > n
    
    q100, r = divmod(r, 100)
    q50, r = divmod(r, 50)
    q20, r = divmod(r, 20)
    q10, r = divmod(r, 10)
    q5, r = divmod(r, 5)
    q2, r = divmod(r, 2)
    
    q = bool(q100) + bool(q50) + bool(q20) + bool(q10) + bool(q5) + bool(q2)
    
    if r == 0 and q == 2:
        print('possible')
    else:
        print('impossible')
