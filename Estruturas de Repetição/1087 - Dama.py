x1 = x2 = y1 = y2 = 1
while x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:
    x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:
        if x1 == x2 and y1 == y2:
            print(0)
        elif x1 == x2 or y1 == y2:
            print(1)
        elif x1 - x2 == y1 - y2 or x1 - x2 == y2 - y1:
            print(1)
        else:
            print(2)


