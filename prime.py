p = [2, ]
n = 2

while len(p) <= 100000:
    i = 0
    while (n % p[i]) != 0:
        if len(p) != (i + 1):
            i = i + 1
        else:
            p.append(n)
            break
    n = n + 1

print(p)
