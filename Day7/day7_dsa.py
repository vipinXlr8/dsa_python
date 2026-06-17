# Two Pointer Two sum
# Target sum = 8 in given array arr = [1,2,3,4,5]

arr= [1,2,3,4,5,6]
#target = 8 o/p [1,4] #0 based indexing ke sath
def two_sum(arr,target):
    left = 0
    right = len(arr)-1
    while(left<right):
        curr_sum=arr[left]+arr[right]
        if curr_sum==target:
            return[left,right]
        elif curr_sum<target:
            left+=1
        else:
            right-=1
    return -1
print(two_sum(arr,8))    



