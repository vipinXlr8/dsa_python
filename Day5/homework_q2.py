#Right Rotate by K
def right_rotate_by_1(arr):
    temp = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = temp

def right_rotate_k(arr, k):
    n = len(arr)
    k = k % n

    for _ in range(k):
        right_rotate_by_1(arr)

    return arr

arr = [1, 2, 3, 4, 5]
print(right_rotate_k(arr, 1))