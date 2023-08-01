from string import ascii_uppercase

while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        tot = 0
        for _ in range(n):
            ent = input()
            tmp = ''
            for i in ent:
                if i not in ascii_uppercase:
                    tmp += i
            tot += int(tmp)
            
        print(tot)
