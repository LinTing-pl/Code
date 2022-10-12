# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S的长度在[1, 500]之间。 
#  S只包含小写字母 'a' 到 'z' 。 
#  
#  Related Topics 贪心 哈希表 双指针 字符串 👍 733 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        dic = {s: index for index, s in enumerate(s)}  # 存储某个字母对应地最后一个序号
        num = 0  # 直接计数
        result = []
        j = dic[s[0]]  # 第一个字符的最后位置

        for i in range(len(s)):  # 逐个遍历
            num += 1  # 找到一个就加1个长度
            if dic[s[i]] > j:  # 思路一样，如果最后位置比刚才的大，就更新最后位置
                j = dic[s[i]]
            if i == j:  # 思路一样，形式不同，这里就是找到这一段的结束了，就说明当前位置的index和这个字母在字典里的最后位置应该是相同的。
                result.append(num)  # 加入result
                num = 0  # 归0
        return result
# leetcode submit region end(Prohibit modification and deletion)
