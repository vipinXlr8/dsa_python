arr = [5, 2, 8, 1, 9, 3]
smallest=arr[0]
for num in arr:
    if num < smallest:
        smallest=num
print(smallest)