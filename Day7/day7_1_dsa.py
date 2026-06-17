# [0,1,0,3,12] move zeroes to end with two pointer

# Dry Run
# 0 1 0 3 12  Slow Pointer -> Where to keep non zero Fast Pointer-> Find non zero element
# S
# F
# Code
def move_zeroes(arr):
    slow=0
    for fast in range(len(arr)):
        if arr[fast]!=0:
            arr[slow],arr[fast]=arr[fast],arr[slow]
            slow+=1
    return arr
arr=[0,1,0,3,12]
print(move_zeroes(arr))

