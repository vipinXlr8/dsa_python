# Two pointer 
# Probblem statment reverse array without extra array

# Dry Run Thinking 
# arr=[12345]
#  start                End
#   Left                Right
#   1                     5
#   swap
#   5                     1
#   4                     2
#   3                     3 Conditon comes here left and right are same
# array is reverse now

# Convert to English
# 1. initialize left to index 0
# 2. initialize right to index -1 len-1
# 3. Swap left and right
#   move left by step 1 forward and right by 1 step backward
# 4 return array
# 

# Code 
arr = [7,2,3,1,5]
def reverese_array(arr):
    left = 0
    right =len(arr)-1
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1  
        right-=1
    return(arr)
print(reverese_array(arr))    
      
