def getHappyString( n: int, k: int) -> str:
    maxN  = 2**(n-1) * 3
    
    if k>maxN:
        return ""
    
    a = 2**(n-1)
    b = 2**(n-1)*2
    ans = [] 
    if k>b:
        ans.append('c')
        k-=b
    elif k>a:
        ans.append('b')
        k-=a
    else:
        ans.append('a')
    
    binLeft = bin(k-1)[2:]
    
    lenB = len(binLeft)

    for i in range(n-1):
        toRight = n-1-i
        if toRight>lenB:
            if ans[-1]=='b':
                ans.append('a')
            else:
                ans.append('b')
        else:
            curr = binLeft[lenB-toRight]

            if curr == '0':
                if ans[-1]=='b':
                    ans.append('a')
                else:
                    ans.append('b')
            else:
                if ans[-1]!='c':
                    ans.append('c')
                else:
                    ans.append('b')
    return "".join(ans)
print(getHappyString(10,100))
