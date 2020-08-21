class Solution:
    def canJump(self, nums) -> bool:
        n=len(nums)
        

        canpoint=0
        for i in range(n):
            if i<=canpoint:
                canpoint=max(canpoint,i+nums[i])

   
        return canpoint>=n-1


sol=Solution()
print(sol.canJump([2,3,1,1,4]))
                        
