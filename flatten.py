lst = [[1],2,[[3, 4], 5],[[[]]],[[[6]]],7,8,[]]
def flattenit(lst):
    res = []
    
    while i<len(lst):
        while True:
            try:
                lst[i:i+1] = lst[i]
            except (TypeError, IndexError):
                break
        i += 1
    return lst

print(flattenit(lst))
    