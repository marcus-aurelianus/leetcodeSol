from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int) :

        q=deque()
        q.append(0)
        for i in range(1,k):
            curr=nums[i]
            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)

        anslist=[]

        n=len(nums)
        for i in range(k,n):
            anslist.append(nums[q[0]])


            while q and q[0]<=i-k:
                q.popleft()
            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)
        anslist.append(nums[q[0]])  
        return anslist

sol=Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
