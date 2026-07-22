a = [-2, -3, 4, -1, -2, 1, 5, -3]

m = c = a[0]

for i in a[1:]:
    c = max(i, c + i)
    m = max(m, c)

print(m)