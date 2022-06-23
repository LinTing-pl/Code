# 给定字符串列表 strs ，返回 它们中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。 
# 
#  最长特殊序列 定义如下：该序列为某字符串 独有的最长子序列（即不能是其他字符串的子序列）。 
# 
#  s 的 子序列可以通过删去字符串 s 中的某些字符实现。 
# 
#  
#  例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括
# "aebdc"、 "aeb" 和 "" (空字符串)。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: strs = ["aba","cdc","eae"]
# 输出: 3
#  
# 
#  示例 2: 
# 
#  
# 输入: strs = ["aaa","aaa","aa"]
# 输出: -1
#  
# 
#  
# 
#  提示: 
# 
#  
#  2 <= strs.length <= 50 
#  1 <= strs[i].length <= 10 
#  strs[i] 只包含小写英文字母 
#  
#  Related Topics 数组 哈希表 双指针 字符串 排序 👍 93 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        list2 = []
        list3 = []
        for i in strs:
            if strs.count(i) >= 2:
                list2.append(i)
        for i in list2:
            strs.remove(i)
        # 上述操作删除重复字符串
        for i in strs:
            for j in list2:
                temp_len = len(i)
                for k in range(temp_len):
                    if i[k] not in j:
                        break
                    if i[k] in j and k != temp_len - 1:
                        j = j[j.index(i[k]) + 1:]
                if k == temp_len - 1 and i[k] in j:
                    list3.append(i)
                    break
        print(strs, "\n", list3)
        for j in list3:
            strs.remove(j)
        # 上述操作删除子字符串
        # print(strs)
        # 下述操作找最长字符串（即最长特殊序列）
        if len(strs) == 0:
            return -1
        len_max = strs[0]
        for i in range(1, len(strs)):
            if len(len_max) < len(strs[i]):
                len_max = strs[i]
        return len(len_max)
# leetcode submit region end(Prohibit modification and deletion)
