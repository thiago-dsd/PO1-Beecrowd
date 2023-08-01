n = int(input())
for _ in range(n):
    a, b = input().split()
    final = ''
    l_a = len(a)
    l_b = len(b)
    if l_a >= l_b:
        maior_str = a
        maior = l_a
        menor = l_b
    else:
        maior_str = b
        maior = l_b
        menor = l_a
    for i in range(menor):
        final += a[i] + b[i]
    
    final += maior_str[i+1:]
    
    print(final)
