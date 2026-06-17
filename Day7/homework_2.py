#Move all even number to beginning 
# [1,3,2,5,6,8]
arr = [1, 3, 2, 5, 6, 8]

def move_even_to_beginning(arr):
    left = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    return arr

print(move_even_to_beginning(arr))