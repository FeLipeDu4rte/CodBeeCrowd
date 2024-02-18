A, B = map(float, input().split())
C, D = map(float, input().split())

dist = ((C - A)**2 + (D - B)**2) ** (1/2)

print("{:.4f}".format(dist))