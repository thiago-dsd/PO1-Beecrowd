num = int(input())
quebrou = 0
for c in range (0, num):
    L, C = input().split()
    L = int(L)
    C = int(C)
    if L > C:
        quebrou += C
print(quebrou)

