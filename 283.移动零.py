#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = 0
        for i in range(len(nums)):
            if right >= len(nums):
                nums[i] = 0
                continue
            while nums[right] == 0 and right < len(nums)-1:
                right += 1
            nums[i] = nums[right]
            right += 1

# @lc code=end

