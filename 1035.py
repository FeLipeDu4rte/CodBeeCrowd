A, B, C, D = map(float, input().split())
def eh_par(A):
    return A % 2 == 0
if B > C and D > A and C+D > A+B and C > 0 and D > 0 and eh_par(A):
    print("Valores aceitos")
else: 
    print("Valores nao aceitos")