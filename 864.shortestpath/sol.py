from itertools import permutations
from copy import deepcopy
def shortestPathAllKeys(grid):
    m=len(grid)
    n=len(grid[0])
    newgrid=[]
    
    for i in range(m):
        newgrid.append(list(grid[i]))
    grid=newgrid

    keys=[]

    itspos={}
    for i in range(m):
        for j in range(n):
            if 'a'<=grid[i][j]<='z':
                keys.append(grid[i][j])
            elif 'A'<=grid[i][j]<='Z':
                itspos[grid[i][j]]=[i,j]
            elif grid[i][j]=='@':
                spoint=[i,j]
                grid[i][j]='.'
    perms=list(permutations(keys))
    
    print(len(perms))
    ans=float("inf")
    for perm in perms:
        startpoint=spoint
        
        currgird=deepcopy(grid)
        currans=0

        keysgot={}
        for ele in perm:
            #print(ele,currans)
            visited=[]
            for i in range(m):
                visited.append([False]*n)
                
            bfs=[startpoint]
            depth=0
            foundkey=False

            while bfs:
                #print(bfs,depth)
                newbfs=[]
                for currpoint in bfs:
                    x,y=currpoint
                    visited[x][y]=True

                        
                        
                    if currgird[x][y]==ele:
                        currgird[x][y]='.'
                        #print(x,y)
                        startpoint=[x,y]
                        currans+=depth
                        foundkey=True
                        itsposition=itspos[ele.capitalize()]
                        nx,ny=itsposition
                        currgird[nx][ny]='.'
                        break
 
                    elif currgird[x][y]=='.':
                        if x>0 and not visited[x-1][y] and (currgird[x-1][y]=='.' or 'a'<=currgird[x-1][y]<='z'):
                            newbfs.append([x-1,y])
                        if x<m-1 and not visited[x+1][y] and (currgird[x+1][y]=='.' or 'a'<=currgird[x+1][y]<='z'):
                            newbfs.append([x+1,y])
                        if y>0 and not visited[x][y-1] and (currgird[x][y-1]=='.' or 'a'<=currgird[x][y-1]<='z'):
                            newbfs.append([x,y-1])
                        if y<n-1 and not visited[x][y+1] and (currgird[x][y+1]=='.' or 'a'<=currgird[x][y+1]<='z'):
                            newbfs.append([x,y+1])
                depth+=1
                bfs=newbfs


            
            if not foundkey:
                currans=float("inf")
                break
        ans=min(currans,ans)
        
    return ans if ans <float("inf") else -1

a=["..Ff..#..e.#...",
   ".....#.##...#..",
   "....#.#...#....",
   "##.......##...#",
   "...@#.##....#..",
   "#........b.....",
   "..#...#.....##.",
   ".#....#E...#...",
   "......A.#D.#...",
   "...#...#..#....",
   "...a.#B#.......",
   ".......c.....#.",
   "....#...C#...#.",
   "##.#.....d..#..",
   ".#..#......#..."]
print(shortestPathAllKeys(a))
    
