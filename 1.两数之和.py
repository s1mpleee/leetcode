#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            if target-num not in hashmap.keys():
                hashmap[num] = idx
            else:
                return [idx, hashmap[target-num]]

# @lc code=end

