def binary(a, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if a[mid] == key:
            return mid
        elif key < a[mid]:
            return binary(a, low, mid - 1, key)
        else:
            return binary(a, mid + 1, high, key)

    return -1

a = [5, 10, 15, 20, 25]
key = 20

result = binary(a, 0, len(a) - 1, key)

if result != -1:
    print("Key found at index", result)
else:
    print("Key not found")