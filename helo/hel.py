def convert(str1):
    n=len(str1)
    stres=[]

    
    for i in range(n):
        if i==0:
            prev=str1[0]
            counter=1
        if i==n-1:
            stres.append([prev,counter])
        else:
            if prev!=str1[i+1]:
                stres.append([prev,counter])
                prev=str1[i+1]
                counter=1
            else:
                counter+=1
    return stres

def cancovert(s1,s2):

    if len(s1)!=len(s2):
        return False
    else:
        n=len(s1)
        for i in range(n):
            if s2[i][0]==s1[i][0] and (s2[i][1]>=3 or s2[i][1]==s1[i][1]):
                continue
            else:
                return False
        return True
print(convert('hello'))
print(cancovert(convert('hello'),convert("heeellooo")))
