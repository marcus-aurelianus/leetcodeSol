from functools import reduce
def powerset(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  lst, [[]])
print(powerset([1,2,3]))







def ps(lst):
    return reduce(lambda result,x: result+[subset+[x] for subset in result],lst,[[]])

print(ps([1,2,3]))


def ps1(lst):
    return reduce(lambda result,x: [[x]+subset for subset in result],lst,[[]])

print(ps1([1,2,3]))
