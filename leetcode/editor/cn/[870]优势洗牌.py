# 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数
# 目来描述。 
# 
#  返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# 输出：[2,11,7,15]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# 输出：[24,32,8,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length <= 10⁵ 
#  nums2.length == nums1.length 
#  0 <= nums1[i], nums2[i] <= 10⁹ 
#  
#  Related Topics 贪心 数组 排序 👍 187 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sortA = sorted(nums1)
        sortB = sorted(nums2)
        assign = {b: [] for b in nums2}
        remain = []
        j = 0
        for nA in sortA:
            if nA > sortB[j]:
                assign[sortB[j]].append(nA)
                j += 1
            else:
                remain.append(nA)
        return [assign[b].pop() if assign[b] else remain.pop() for b in nums2]
# leetcode submit region end(Prohibit modification and deletion)
