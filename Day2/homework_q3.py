arr = [5, 2, 8, 1, 9, 3]

smallest = second_smallest = float('inf')

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest and num != smallest:
        second_smallest = num

print(second_smallest)