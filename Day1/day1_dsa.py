#Arrays
#largest element in an Array
# marks = [65,78,92,81,75]
# indexing --> 0 to n-1 --> 0 to 4
#step1 : understand the problem
#1. highest = 65
#2 78  -> Highest = 78
#3 92 ->            92
#4 81 ->            92
#5 75               92

# Step 2: convert thinking into english
# 1. store first element in highest variable
# 2. Traverse all remainaing elements
# 3. Compare current marks with highest one
# 4. update highest variable if current element is larger/highest
# 5. 2-4 step repeat -- > loop -- > for loop
# 6. return highest

# Step 3: convert above English into code
marks = [65,78,92,81,75]
highest=marks[0]
for mark in marks:
    if mark > highest:
        highest=mark
print(highest)

