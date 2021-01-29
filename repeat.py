def maxConti(lst):
    currTemp = 0
    curMax = 0
    allNeg = True
    maxNum = -float("inf")
    for ele in lst:
        maxNum = max(maxNum,ele)
        if ele>0:
            allNeg = False
            currTemp += ele 
            currMax = max(currTemp,curMax)
        else:
            if (currTemp+ele)>=0:
                currTemp+=ele
            else:
                currTemp=0 
    return maxNum if allNeg else currMax



print(maxConti([-2,1,-3,4,-1,2,1,-5,4,9]))
