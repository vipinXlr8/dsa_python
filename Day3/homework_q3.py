# Count Occurance of target = 2
arr = [5, 3, 2, 6, 2, 7, 8, 2]
target = 2

def count_occurrence(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count

print(count_occurrence(arr, target))