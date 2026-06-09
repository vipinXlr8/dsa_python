arr = [5, 2, 8, 1, 9, 3]

largest = second_largest = third_largest = float('-inf')

for num in arr:
    if num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        third_largest = second_largest
        second_largest = num

    elif num > third_largest and num != second_largest and num != largest:
        third_largest = num

print(third_largest)