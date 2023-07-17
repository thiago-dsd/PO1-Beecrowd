num = int(input())
for i in range (2, 10000, num):
    if i % num == 2:
        print(i)

