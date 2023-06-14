#COORDERNADAS TERRENO A
xaA, yaA = input().split()
xbA, ybA = input().split()
xcA, ycA = input().split()
xdA, ydA = input().split()
#COORDENADAS TERRENO B
xaB, yaB = input().split()
xbB, ybB = input().split()
xcB, ycB = input().split()
xdB, ydB = input().split()
xaA, yaA, xbA, ybA, xcA, ycA, xdA, ydA = int(xaA), int(yaA), int(xbA), int(ybA), int(xcA), int(ycA), int(xdA), int(ydA) 
xaB, yaB, xbB, ybB, xcB, ycB, xdB, ydB = int(xaB), int(yaB), int(xbB), int(ybB), int(xcB), int(ycB), int(xdB), int(ydB)
areaA = (abs((xaA*ybA + xbA*ycA + xcA*ydA + xdA*yaA) - (yaA*xbA + ybA*xcA + ycA*xdA + ydA*xaA))/2)
areaB = (abs((xaB*ybB + xbB*ycB + xcB*ydB + xdB*yaB) - (yaB*xbB + ybB*xcB + ycB*xdB + ydB*xaB))/2)

if areaA > areaB:
    print("terreno A")
else:
    print("terreno B")

