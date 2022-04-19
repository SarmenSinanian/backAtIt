# Given an integer array nums of length n, you want to create
# an array ans of length 2n where ans[i] == nums[i] and
# ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in nums:
            nums1.append(i)
        nums2 = nums1*2
        return nums2