name=input()
sal=float(input())
tv=float(input())

tv = ((tv/100) * 15)
X = sal+tv

print("TOTAL = R$ {:.2f}".format(X))