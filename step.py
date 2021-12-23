import matplotlib.pyplot as plt

p = [2, ]
n = 2
x = []
y = []
b = 0

while n <= 100:
    i = 0
    while (n % p[i]) != 0:
        if len(p) != (i + 1):
            i = i + 1
        else:
            p.append(n)
            b = b + 1
            break
    
    x.append(n)
    y.append(len(p))
    n = n + 1

print(len(p))
#print(len(x))
#print(len(y))
print(p)
#print(y)

plt.scatter(x, y)
plt.show()
