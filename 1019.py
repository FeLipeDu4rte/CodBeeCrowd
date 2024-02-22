ts = int(input())

H = int(ts / 3600)
ts %= 3600

M = int(ts / 60)
S = ts % 60

print("{}:{}:{}".format(H, M, S))