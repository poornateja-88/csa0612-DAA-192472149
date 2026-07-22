import heapq

a = [4, 10, 3, 5, 1]
heapq.heapify(a)

while a:
    print(heapq.heappop(a), end=" ")