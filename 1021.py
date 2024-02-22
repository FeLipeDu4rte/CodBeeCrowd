def imprimirQuantidade(valor, tipo, valorUnitario):
    quantidade = int(valor / valorUnitario)
    print("{} {}(s) de R$ {:.2f}".format(quantidade, tipo, valorUnitario / 100))
    return valor % valorUnitario

valor = float(input())

centavos = int((valor * 100))

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]
j = 0
k = 0

print("NOTAS:")
while j != 6:
    centavos = imprimirQuantidade(centavos, "nota", notas[j])
    j +=1

print("MOEDAS:")
while k != 6:
    centavos = imprimirQuantidade(centavos, "moeda", moedas[k])
    k +=1