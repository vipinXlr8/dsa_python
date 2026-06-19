
def min_subarray_length(arr,target):
    window_sum = 0
    min_length = len(arr)+1
    left_pointer = 0
    for right_pointer in range(len(arr)):
        window_sum=window_sum + arr[right_pointer]
        while window_sum >= target:
            current_length = right_pointer-left_pointer+1
            if current_length < min_length:
                min_length=current_length

            window_sum=window_sum - arr[left_pointer]
            left_pointer+=1
        
    if min_length==len(arr)+1:
        return 0

    return min_length
arr = [2,3,1,2,3,4]
target = 7
print(min_subarray_length(arr, target))