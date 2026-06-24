# Two Sum 
# with two pointer condition was array is sorted 
# when is array is not sorted --> hashmap

def two_sum(arr,target):
    seen={}
    for i in range(len(arr)):
        curr_num=arr[i]
        complement=target-curr_num
        if complement in seen:
            return [seen[complement],i]
        seen[curr_num]=i
nums=[2,7,1,15]
target=9
print(two_sum(nums,target))