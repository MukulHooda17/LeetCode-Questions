# Find all duplicates
def find_duplicates(nums):
    d = {}

    for num in nums:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1

    a = []

    for key in d.keys():
        if d[key] == 2:
            a.append(key)