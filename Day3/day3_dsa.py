#Travesral + Search pattern
#What is Linear Search
#Array ke elements ko ek ek karke search karna jab tak target na mil jaye
#Element Exist or not

# arr = [5,2,8,1,9]
# target=8
# Current Element   Target      Match?
# 5                   8           No
# 2                   8           No
# 8                   8           Yes   return true

# Convert into english
# 1. Travers the array 
# 2. Compare current element with target
# 3. If they match --> Return yes
# 4. If loop finish --> return No or False

#Convert to code
arr = [5,2,8,1,9]
target=8
def linear_search(arr,target):
    for curr_num in arr:
        if curr_num===target:
            return True
    return False
print(linear_search(arr,target))
    
#Travesral + Find Index
# 1. Traverse the array with Index
# 2. Compare current element with target
# 3. If They Match, return Index
# 4. After loop finishes return -1

def return_index(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr2 = [5,2,8,1,9]
print(return_index(arr2,target))