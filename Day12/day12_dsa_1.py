# Boyer Moore voting algo

def moore_algorithm(arr):
    candidate=None
    vote=0
    for num in arr:
        if vote ==0:
            candidate=num
        if num==candidate:
            vote+=1
        else:
            vote-=1
    return candidate
arr=[2,2,1,1,1,2,2]
print(moore_algorithm(arr))
# note this algorithm makes more sense when there is definelty more than one element
# if unique exists then algo will not work