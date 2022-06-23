# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。 
# 
#  示例 1 : 
# 
#  
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
#  
# 
#  示例 2 : 
# 
#  
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
#  
# 
#  注意: 
# 
#  
#  给定数字的范围是 [0, 10⁸] 
#  
#  Related Topics 贪心 数学 👍 240 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)  # int-->str
        List1 = list(s)  # str-->list
        l = len(List1)
        List2 = sorted(List1, reverse=True)  # 降序排序
        if List1 == List2:  # 排序后的列表与原列表相等就直接返回
            return num
        m = 0
        while m < l and List1[m] == List2[m]:  # 找出第一个不相等的位置
            m += 1
        for i in range(l - 1, -1, -1):  # 逆序遍历
            if List1[i] == List2[m]:
                List1[m], List1[i] = List1[i], List1[m]  # 交换位置
                break
        return int(''.join(List1))
# leetcode submit region end(Prohibit modification and deletion)
