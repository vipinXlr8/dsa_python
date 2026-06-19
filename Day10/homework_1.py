#Find the element with max frequency
def max_frequency_element(arr):
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = 0
    max_element = None

    for key, value in frequency.items():
        if value > max_freq:
            max_freq = value
            max_element = key

    return max_element


arr = [2, 1, 2, 3, 1, 2, 4]

print(max_frequency_element(arr))