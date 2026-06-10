#1 First Occurance Target = 2
#arr= [5,3,2,6,2,7,8,2]
def first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 2, 6, 2, 7, 8, 2]
target = 2

print(first_occurrence(arr, target))