A, B, C = map(int, input().split())

MaiorAB = (A+B+abs(A-B))/2
MaiorABC = (MaiorAB + C + abs(MaiorAB-C))/2

print("{:.0f} eh o maior".format(MaiorABC))