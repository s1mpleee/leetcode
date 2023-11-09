#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            if str(sorted([i for i in string])) in result.keys():
                result[str(sorted([i for i in string]))].append(string)
            else:
                result[str(sorted([i for i in string]))] = [string]
        return list(result.values())
# @lc code=end

