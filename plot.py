import matplotlib.pyplot as plt

p = [2, ]
x = [1, ]
n = 2

while n <= 100:
    i = 0
    while (n % p[i]) != 0:
        if len(p) != (i + 1):
            i = i + 1
        else:
            p.append(n)
            x.append(x[len(x) - 1] + 1)
            break
    n = n + 1

print(len(x))
print(len(p))
print(p)

plt.plot(x, p)
plt.show()
