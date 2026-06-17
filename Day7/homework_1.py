#move all -ve number to begining 
# [1,2,3,-1,-2,6]
arr = [1, 2, 3, -1, -2, 6]

def move_negative_to_beginning(arr):
    left = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    return arr

print(move_negative_to_beginning(arr))