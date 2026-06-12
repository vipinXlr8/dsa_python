# Array Manipulation 
# [1,2,3,4,5] --> [5,4,3,2,1]

#1 Reverse Array
arr=[1,2,3,4,5]
#O/p : [5,4,3,2,1]
def reverse_array(arr):
    rev_array=[]
    for i in range(len(arr)-1,-1,-1):
        rev_array.append(arr[i])
    return rev_array
print(reverse_array(arr))
