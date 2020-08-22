def array_diff(a, b):
    a = set(a)
    b = set(b)
    return [item for item in a - b if item == b]
    
print(array_diff([1,2], [1]))