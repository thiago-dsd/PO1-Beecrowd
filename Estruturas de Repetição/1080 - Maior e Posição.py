num = 0
pos = 0
posnum = 0
for i in range (0, 100):
    pos +=1
    a = int(input())
    if a > num:
        posnum = pos
        num = a
print(num)
print(posnum)
