from string import ascii_lowercase as alfabeto


n = int(input())

for _ in range(n):
    palavra = input()
    final = ''
    for i in palavra[::-1]:
        if i in alfabeto:
            final += i
            
    print(final)
