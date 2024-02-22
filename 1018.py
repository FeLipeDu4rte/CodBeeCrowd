valor = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
j = 0

print(valor)
while j != 7:
    qtd_notas = int(valor / cedulas[j])
    valor %= cedulas[j]
    x = cedulas[j]
    j += 1

    print("{} nota(s) de R$ {:.2f}".format(qtd_notas, x).replace('.', ','))