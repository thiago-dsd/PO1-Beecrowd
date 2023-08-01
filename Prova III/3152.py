A = []
B = []
for _ in range(4):
    A.append(tuple([int(x) for x in input().split()]))

for _ in range(4):
    B.append(tuple([int(x) for x in input().split()]))

A = sorted(A, key=lambda x: x[0])
B = sorted(B, key=lambda x: x[0])

det_1A = abs(A[1][1]*A[2][0] + A[2][1]*A[0][0] + A[0][1]*A[1][0] - A[0][0]*A[1][1] - A[0][1]*A[2][0] - A[1][0]*A[2][1])
det_2A = abs(A[2][1]*A[3][0] + A[3][1]*A[1][0] + A[1][1]*A[2][0] - A[1][0]*A[2][1] - A[1][1]*A[3][0] - A[2][0]*A[3][1])

area_A =  .5*det_1A + .5*det_2A

det_1B = abs(B[1][1]*B[2][0] + B[2][1]*B[0][0] + B[0][1]*B[1][0] - B[0][0]*B[1][1] - B[0][1]*B[2][0] - B[1][0]*B[2][1])
det_2B = abs(B[2][1]*B[3][0] + B[3][1]*B[1][0] + B[1][1]*B[2][0] - B[1][0]*B[2][1] - B[1][1]*B[3][0] - B[2][0]*B[3][1])

area_B =  .5*det_1B + .5*det_2B

if area_A > area_B:
    print('terreno A')
else:
    print('terreno B')
