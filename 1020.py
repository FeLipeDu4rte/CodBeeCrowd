t = int(input())

ano = int(t / 365)
t %= 365

mes = int(t / 30)
sem = t % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, sem))