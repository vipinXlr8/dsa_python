# leetcode 217 --> contains duplicate using hashset

def containsduplicate(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return True
        seen.add(num)

    return False

arr = [5, 3, 8, 3]
print(containsduplicate(arr))  