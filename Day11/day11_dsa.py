#Hashing 
# Hashmap and Hashset
# Leetcode 217

# Given an Integer array nums return true if duplicate occurs

def contains_duplicate(arr):

    seen={}
    for num in arr:
        if num in seen:
            return True
        seen[num]="True,Visited"
    return False
arr=[1,2,3,4]
arr2=[1,2,3,1]
print(contains_duplicate(arr))
print(contains_duplicate(arr2))