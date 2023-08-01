n = int(input())

c = e = 0
tmp_c = tmp_e = 0
for _ in range(n):
    c_ida, c_volta = [x[0] == 'c' for x in input().split()]
    
    if c_ida:
        if tmp_c > 0:
            tmp_c -= 1
            tmp_e += 1  # vai p escritorio
        else:
            c += 1
            tmp_e += 1  # foi da casa p escritorio
    
    if c_volta:
        if tmp_e > 0:
            tmp_e -= 1
            tmp_c += 1  # vai p casa
        else:
            e += 1
            tmp_c += 1  # foi do escritorio p casa

print(c, e)
