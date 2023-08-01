fib = [1, 1]
three = []
while len(three) != 60:
    new = fib[-2] + fib[-1]
    fib.append(new)
    if new % 3 == 0 or '3' in str(new):
        three.append(new)
    
while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        print(three[n-1])
