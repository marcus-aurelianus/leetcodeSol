import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        dic={}
        for i in range(n):
            loc=dic.get(manager[i],[])
            loc.append(i)
            dic[manager[i]]=loc
        dfs=[[headID,0]]
        res=0

        #print(dic)
        while dfs:
            #print(bfs,res)
            emp,time=dfs.pop()

            newloc=dic.get(emp,[])
            if not newloc:
                res=max(res,time)
                continue
            new_time=time+informTime[emp]
            for empn in newloc:
                dfs.append([empn,new_time])
        

        return res


sol=Solution()

print(sol.numOfMinutes(11,4,[5,9,6,10,-1,8,9,1,9,3,4],[0,213,0,253,686,170,975,0,261,309,337]))
