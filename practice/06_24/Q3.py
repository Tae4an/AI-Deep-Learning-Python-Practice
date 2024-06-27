def func(lst):
    res = max(lst)

    idx = lst.index(res)

    return [res, idx]

print(func([1, 5, 3, 9, 12])) 
