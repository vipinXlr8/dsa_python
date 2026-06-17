# Sliding Window
# Maximun sum subarray of size K
# 3 consecutive element ka max sum

# arr = [2,1,5,1,3,2]
# k = 3
# slinding windown = old sum- outgoing element + incoming element
def max_sum(arr,k):
    window_sum=0
    for i in range(k):
        window_sum+=arr[i]
    max_sum = window_sum
    for end in range(k,len(arr)):
        window_sum=window_sum-arr[end-k]+arr[end]
        if window_sum>max_sum:
            max_sum=window_sum
    return max_sum
arr = [2,1,5,1,3,9]
k = 3
print(max_sum(arr,k))