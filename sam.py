def convertToTitle( n: int) -> str:
    ans=[]
    n-=1
    while n>=0:
        curr=n%26
        ans=[curr]+ans
        n//=26
        n-=1
    return "".join([chr(i+65) for i in ans])

print(convertToTitle(1))

def spiralOrder(matrix):
    ans=[]
    def getans(arr, i, j, m, n): 

        # If i or j lies outside the matrix  
        if (i >= m or j >= n): 
            return; 

        # Print First Row  
        for p in range(i, n): 
            ans.append(arr[i][p])

        # Print Last Column  
        for p in range(i + 1, m): 
            ans.append(arr[p][n - 1])

        # Print Last Row, if Last and  
        # First Row are not same  
        if ((m - 1) != i):  
            for p in range(n - 2, j - 1, -1): 
                ans.append(arr[m - 1][p])

        # Print First Column, if Last and  
        # First Column are not same  
        if ((n - 1) != j): 
            for p in range(m - 2, i, -1): 
                ans.append(arr[p][j])

        getans(arr, i + 1, j + 1, m - 1, n - 1)     
    getans(matrix,0,0,len(matrix),len(matrix[0]))  
    return ans
print(spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]))
