#Hashing
#Rule Store once use many times

# 1. Create Empty Storage
# 2. Traverse Array
# 3. if number is seen for first time store its freq as 1
#     otherwise increase by 1
# 4. return frequencies

def frequency_count(arr):
    frequency={}
    for num in arr:
        if num not in frequency:
            frequency[num]=1
        else:
            frequency[num]+=1
    return frequency
arr=[2,1,2,3,1,2,4]
print(frequency_count(arr))
# frequency = {} #dict {key->value}->{number->freq}

