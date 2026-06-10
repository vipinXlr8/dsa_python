#1 Second Occurance Target = 2
#arr= [5,3,2,6,2,7,8,2]

arr = [5, 3, 2, 6, 2, 7, 8, 2]
target = 2

def second_occurrence(arr, target):
    count = 0

    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
            if count == 2:
                return i

    return -1

print(second_occurrence(arr, target))