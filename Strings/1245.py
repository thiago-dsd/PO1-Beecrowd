while True:
    try:
        n = int(input())
    except:
        break
    else:
        nums = {str(x): [] for x in range(30, 61)}
        for _ in range(n):
            tam, pe = input().split()
            nums[tam].append(pe)
        
        pares_validos = 0
        for v in nums.values():
            e = d = 0
            for i in v:
                if i == 'E':
                    e += 1
                else:
                    d += 1
            if e <= d:
                pares_validos += e
            else:
                pares_validos += d
        
        print(pares_validos)
