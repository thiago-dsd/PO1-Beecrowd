n = int(input())

figs = []
rep = 0
for _ in range(n):
    fig = input()
    if fig not in figs:
        figs.append(fig)
    else:
        rep += 1

print(len(figs))
print(rep)
