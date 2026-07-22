import math

p = [(1, 2), (4, 5), (7, 8), (3, 1)]

d = math.dist(p[0], p[1])
pair = (p[0], p[1])

for i in range(len(p)):
    for j in range(i + 1, len(p)):
        x = math.dist(p[i], p[j])
        if x < d:
            d = x
            pair = (p[i], p[j])

print(pair)
print("Distance =", d)