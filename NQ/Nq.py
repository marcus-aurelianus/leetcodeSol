SIZE=4

def findallNquenn(row,cols,res):
    if row==SIZE:
        res.append(cols[:])
    else:
        for col in range(0,SIZE):
            if check1(cols,row,col):
                cols[row]=col
                findallNquenn(row+1,cols,res)

def check1(cols,row1,col1):
    for row2 in range(0,row1):
        col2=cols[row2]


        if col1==col2:
            return False

        colDisance=abs(col2-col1)

        rowDistance=row1-row2


        if colDisance==rowDistance:
            return False
    return True


lis=[]

init=[[]]*SIZE
findallNquenn(0,init,lis)
print(lis)
