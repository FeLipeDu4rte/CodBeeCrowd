import math
a, b, c= map(float, input().split())
x = float((b**2) - (4*a*c))

if x > 0 and a != 0:
    X1 = math.sqrt(x)
    R1 = (-b + X1)/(2*a)
    print("R1 = {:.5f}".format(R1))
    R2 = (-b - X1)/(2*a)
    print("R1 = {:.5f}".format(R2))
else:
    print("Impossivel calcular")
    