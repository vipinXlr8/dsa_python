#Traversal + Accumulation Pattern

#sum of array

# arr = [5,2,8,1]

#o/p sum -->16

#Current Number             Running Total
# Start                         0
# 5                             5
# 2                             7
# 8                             15
# 1                             16

# Convert to English 
# 1. create variable total and initialize with 0
# 2. Traverse the array 
# 3. Add Current element to total
# 4. After loop end, return total

#Convert to code
arr = [5,2,8,1]
total = 0
for num in arr:
    #total = total + num
    total+=num
print(total)