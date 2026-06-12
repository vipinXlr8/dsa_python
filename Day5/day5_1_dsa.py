#left rotate
#arr= [1,2,3,4,5]

#o/P : [2,3,4,5,1]

#DRY Run        Index       0 1 2 3 4 
# # first = 1                 1,2,3,4,5
#     i           i+1
# arr[0]=arr[1]               2 2 3 4 5
# arr[1]=arr[2]               2 3 3 4 5
# arr[2]=arr[3]               2 3 4 4 5
# arr[3]=arr[4]               2 3 4 5 5
# arr[4]=first                2 3 4 5 1
# arr[-1]=first               2 3 4 5 1    


#Thinking to English
# 1.store first element in temp variable
# 2. Shift all remaning elements one pos to left
# 3. put store element (temp) at last pos -1
# 4. return array

# English into code
arr = [1,2,3,4,5]
def left_rotate_1(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=temp
    return arr
arr=[1,2,3,4,5]
print(left_rotate_1(arr))

