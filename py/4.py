class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = 4
        if n % 2 == 0:
            print(merged)
            return n // 2 - 1, n // 2
            # return (merged[n // 2 - 1] + merged[n // 2]) / 2
        # else:
        #     return merged[n // 2]

# Driver code
sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2,5]))    