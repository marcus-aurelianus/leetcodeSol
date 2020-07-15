


def mergeTwo(lst1,lst2):
    m,n=len(lst1),len(lst2)
    i,j=0,0
    ans=[]
    while i<m or j<n:
        if i<m:
            if j<n:
                if lst1[i]<lst2[j]:
                    ans.append(lst1[i])
                    i+=1
                else:
                    ans.append(lst2[j])
                    j+=1
            else:
                ans.append(lst1[i])
                i+=1
        else:
            ans.append(lst2[j])
            j+=1
    return ans


print(mergeTwo([1,3,4,5],[1,4,7]))
