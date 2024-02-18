A, B, C = map(float, input().split())
D, E, F = map(float, input().split())

X = (B*C) + (E*F)

print("VALOR A PAGAR : R$ {:.2f}".format(X))