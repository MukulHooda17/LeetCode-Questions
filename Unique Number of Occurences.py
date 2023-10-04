# Unique Number of Occurences
def Unique(ls):
    d = {}

    for num in ls:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1

    print(len(d), len(set(d.values())))
    if len(d) == len(set(d.values())):
        return True
    else:
        return False


original = [1, 2, 424, 43, 23, 2]
print(original)
a = original

Unique(a)
