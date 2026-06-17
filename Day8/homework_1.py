# Average of every window of size k
# [2,1,5,1,3,9]
def max_average(arr, k):
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    for end in range(k, len(arr)):
        window_sum = window_sum - arr[end - k] + arr[end]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum / k

arr = [2, 1, 5, 1, 3, 9]
k = 3

print(max_average(arr, k))