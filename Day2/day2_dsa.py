#Find Second Largest Element
#Make 2 variabels Largest ,Second Largest

arr= [5,2,8,1,9,3]
#largest            second largest
# 5                     float(-inf) negative infinity
# 5                         2
# 8                         5
# 9                         8

#Convert into English
#1. Assume first element as largest
#2. Assume second largest is a very small number ---> float('-inf')
#3 Travere the Array 
#4. Compare : if current element is greator than largest
                # Move largest into second largest
                # update largest
#5. else if current element is greator than second largest :- update second largest
#6 3-5 loop
#7 return second largest

#Convert into code
arr = [5, 2, 8, 1, 9, 3]

largest = second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

#Time complexity o(n) 
#Space complexity o(1) 