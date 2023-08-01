fib = [1, 1]
while len(fib) != 40:
    fib.append(fib[-1] + fib[-2])

n = int(input())
acc = []
for c in fib[:n]:
    acc.insert(0, c)

print(' '.join([str(x) for x in acc]))
