











def maxWater(tank):
    n = len(tank)
    maxLeft = [0]*n
    maxRight = [0]*n
    maxLeftCurr = 0
    maxRightCurr = 0
    for i in range(n):
        left = tank[i]
        right = tank[n-1-i]
        maxLeftCurr = max(left,maxLeftCurr)
        maxLeft[i] = maxLeftCurr
        maxRightCurr = max(right,maxRightCurr)
        maxRight[n-1-i] = maxRightCurr
    #print(maxLeft)
    #print(maxRight)
    #print(tank)
    ans = 0 
    for i in range(n):
        ans += max(min(maxLeft[i],maxRight[i])-tank[i],0)
        #print(i,ans)
    return ans
sampleInput = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sampleInput2 = [2,1,2,1,2]


def maxWaterTwo(tank):
    currMax,currRevMax = 0, 0 
    n = len(tank)
    ans = 0
    temAns,temRevAns = 0, 0
    for i in range(n):
        curr = tank[i]
        revCurr = tank[n-1-i]
        if curr<currMax:
            temAns += currMax-curr
        else:
            ans += temAns
            currMax = curr
            temAns = 0

        if revCurr<=currRevMax:
            temRevAns += currRevMax-revCurr
        else:
            ans += temRevAns
            currRevMax = revCurr
            temRevAns = 0

    return ans
print(maxWater(sampleInput2))
print(maxWaterTwo(sampleInput2))
