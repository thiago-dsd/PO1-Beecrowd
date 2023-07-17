def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto
    return a

num = int(input())
for c in range (num):
    a1, b1 = input().split()
    a1, b1 = int(a1), int(b1)
    print(mdc(a1, b1))


