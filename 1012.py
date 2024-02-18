pi = 3.14159
A, B, C = map(float, input().split())

tri = A * C/2 
print("TRIANGULO: {:.3f}".format(tri))
cir = pi * C**2 
print("CIRCULO: {:.3f}".format(cir))
tra = (A+B)*C/2 
print("TRAPEZIO: {:.3f}".format(tra))
qua = B**2 
print("QUADRADO: {:.3f}".format(qua))
ret = A * B 
print("RETANGULO: {:.3f}".format(ret))