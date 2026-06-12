# Find Even number in array

def count(arr):
    count = 0
    for num in arr:
        if num%2 ==0:
            count+=1
    return count

arr=[2,5,6,8,10]
print(count(arr))