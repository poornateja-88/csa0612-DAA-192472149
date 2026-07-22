def quick(a):
    if len(a) <= 1:
        return a
    p = a[0]
    left = [x for x in a[1:] if x <= p]
    right = [x for x in a[1:] if x > p]
    return quick(left) + [p] + quick(right)

a = [10, 7, 8, 9, 1, 5]
print(quick(a))