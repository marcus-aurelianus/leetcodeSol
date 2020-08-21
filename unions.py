def removeStones(points):
    UF = {}
    def find(x):
        if x != UF[x]:
            UF[x] = find(UF[x])
        return UF[x]
    def union(x, y):
        UF.setdefault(x, x)
        UF.setdefault(y, y)
        UF[find(x)] = find(y)

    for i, j in points:
        union(i, ~j)
    print(UF)
    res={find(x) for x in UF}
    print(UF,res)
    return len(points) - len(res)

print(removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
