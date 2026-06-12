# Left rotate by K
arr = [1, 2, 3, 4, 5]

def left_rotate_1(arr):
    temp = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = temp

def left_rotate_k(arr, k):
    n = len(arr)
    k = k % n

    for _ in range(k):
        left_rotate_1(arr)

    return arr

print(left_rotate_k(arr, 3))