def min_subarray(arr, target):
    window_sum = 0
    min_length = len(arr) + 1
    left = 0

    start = end = -1

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= target:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                start = left
                end = right

            window_sum -= arr[left]
            left += 1

    if start == -1:
        return []

    return arr[start:end+1]


arr = [2, 3, 1, 2, 3, 4]
target = 7

print(min_subarray(arr, target))