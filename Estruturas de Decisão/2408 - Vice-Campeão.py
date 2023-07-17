dados = input()
A, B, C = dados.split()
A = int(A)
B = int(B)
C = int(C)
if (B >= A and B <= C) or (B >= C and B <= A):
    print(B)  
elif (A >= B and A <= C) or (A >= C and A <= B):
    print(A)
elif (C >= B and C <= A) or (C >= A and C <= B):
    print(C)

