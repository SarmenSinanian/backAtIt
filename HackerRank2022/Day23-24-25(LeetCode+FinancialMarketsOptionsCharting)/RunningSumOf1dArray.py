# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

nums = [3,1,2,10,1]

sums = []
for i in nums:
    sums.append(i)
    print(sum(sums))

'''actual solution below'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        for i in range(len(nums)):
            sums = sums + nums[i]
            nums[i] = sums
        return nums
'''actual solution above'''