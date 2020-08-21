def largestRectangleArea( heights) -> int:
    if len(heights)==0:
        return 0
    stk=[]
    
    maxsum, n = 0, len(heights)
    for i in range(n+1):
        nowRect=-1
        if i<n:
            nowRect=heights[i]
        while stk and nowRect<=heights[stk[-1]]:
            thisH=heights[stk.pop()]
            thisW=i
            if stk:
                thisW=i-stk[-1]-1
            maxsum=max(maxsum,thisW*thisH)
        stk.append(i)
        print(i,stk,maxsum)
    return maxsum
print(largestRectangleArea([2,1,5,6,6,2,3]))
