#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num-1 not in result.keys() and num+1 not in result.keys():
                result[num] = 1
            elif num-1 in result.keys() and num+1 not in result.keys():
                result[num] = result[num-1] + 1
                result[num-1] = result[num]
            elif num-1 not in result.keys() and num+1 in result.keys():
                result[num] = result[num+1] + 1
                result[num+1] = result[num]
            else:
                result[num] = result[num-1] + result[num+1] + 1
                result[num-1] = result[num+1] = result[num]
        
        return max(list(result.values()))
# @lc code=end

