x = float(input())
y=0
z=25
t = "["
while y != 100:
    if x >= y and x <= z:
        print("Intervalo {}{},{}]".format(t,y,z))
        break
    t = "("
    y +=25
    z +=25
if x < 0 or x > 100:
    print("Fora de intervalo")
