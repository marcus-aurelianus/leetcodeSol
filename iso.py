def isIsomorphic(s: str, t: str) -> bool:
    n=len(s)

    dic={}
    dic1={}
    for i in range(n):
        ino=dic.get(s[i],False)
        ino1=dic1.get(t[i],False)
        if not ino:
            dic[s[i]]=t[i]

        else:
            if ino != t[i]:
                return False
        if not ino1:
            dic[t[i]]=s[i]

        else:
            if ino1 != s[i]:
                return False     
    return True
print(isIsomorphic("ab","aa"))
