class Solution:
    def maxAscendingSum(self, nums) -> int:
        longest = nums[0] 
        for i in range(len(nums) - 1):
            ascend = nums[i]
            nums_before = 0
            for j in range(i, len(nums)):
                if nums[i] < nums[j] and nums_before < nums[j]:
                    print(nums[i], nums[j], nums_before)
                    ascend += nums[j]
                    nums_before = nums[j]
                elif nums[i] >= nums[j] or nums_before > nums[j]:
                    pass
            if ascend > longest:
                longest = ascend      
        return longest  

    

if __name__ == "__main__":
    nums = [10,20,30,5,10,50]
    s = Solution()
    print(s.maxAscendingSum(nums))