def hanoi(n, s, h, d):
    if n == 1:
        print(s, "->", d)
    else:
        hanoi(n-1, s, d, h)
        print(s, "->", d)
        hanoi(n-1, h, s, d)

hanoi(3, "A", "B", "C")