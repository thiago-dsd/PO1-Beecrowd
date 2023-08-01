entrada = input().split()

final = ''
for p in entrada:
    for i in range(1, len(p), 2):
        final += p[i]
    final += ' '

final = final.removesuffix(' ')
print(final)
