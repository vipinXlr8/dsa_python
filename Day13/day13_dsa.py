# Majority Element 
# Leetcode --> 229
# Q => return all element which appear more than n/3
def majorityelement2(arr):
    candidate1 = None
    candidate2 = None

    vote1=0
    vote2=0
    # Find potential candidate in one pass
    for num in arr:
        if candidate1==num:
            vote1+=1
        elif candidate2==num:
            vote2+=1
        elif vote1==0:
            candidate1=num
            vote1=1
        elif vote2==0:
            candidate2=num
            vote2=1
    # verify candidates
    count1=0
    count2=0
    for num in arr:
        if num==candidate1:
            count1+=1
        elif num==candidate2:
            count2+=1
        result=[]

        if count1>len(arr)//3:
            result.append(candidate1)
        if count2>len(arr)//3:
            result.append(candidate2)
    return result
arr=[1,2,3,1,2,1,2,1,2]
print(majorityelement2(arr))