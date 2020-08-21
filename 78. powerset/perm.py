from itertools import permutations

print([list(x) for x in permutations([1,2,2])])
def permuteUnique( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    n = len(nums)
    res = []
        
    def dfs(nums, l):
        if l >= n:
            res.append(list(nums))
            return 
        for i in range(l, n):
            toc=True
            for j in range(l+,i):
                if nums[j]==nums[i]:
                    toc=False
                    break
            if toc:
                nums[l], nums[i] = nums[i], nums[l]  # swap
                dfs(nums, l+1)  # note now we're passing by reference
                nums[i], nums[l] = nums[l], nums[i]

    nums.sort()
    dfs(nums, 0)
    return res

print(permuteUnique([1,2,2]))
