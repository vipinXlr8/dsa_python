#Hashmap
# Leetcode Question Majority Element (169)
# arr=[2,2,1,1,1,2,2] majority --> n/2 times 7/2 = 3.5
# o/p : 2

def majority_element(arr):
    freq={}
    
    for num in arr:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
    limit=len(arr)//2
    for num in freq:
        if freq[num]>limit:
            return num
        
arr=[2,2,1,1,1,2,2]
print(majority_element(arr))