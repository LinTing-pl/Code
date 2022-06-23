# 给定一个数字字符串 num，比如 "123456579"，我们可以将它分成「斐波那契式」的序列 [123, 456, 579]。 
# 
#  形式上，斐波那契式 序列是一个非负整数列表 f，且满足： 
# 
#  
#  0 <= f[i] < 2³¹ ，（也就是说，每个整数都符合 32 位 有符号整数类型） 
#  f.length >= 3 
#  对于所有的0 <= i < f.length - 2，都有 f[i] + f[i + 1] = f[i + 2] 
#  
# 
#  另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。 
# 
#  返回从 num 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num = "1101111"
# 输出：[11,0,11,11]
# 解释：输出[110,1,111]也可以。 
# 
#  示例 2： 
# 
#  
# 输入: num = "112358130"
# 输出: []
# 解释: 无法拆分。
#  
# 
#  示例 3： 
# 
#  
# 输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num.length <= 200 
#  num 中只含有数字 
#  
#  Related Topics 字符串 回溯 👍 254 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        ans = list()

        def backtrack(index):
            if index == len(num):
                return len(ans) >= 3

            curr = 0
            for i in range(index, len(num)):
                if i > index and num[index] == "0":
                    break
                curr = curr * 10 + ord(num[i]) - ord("0")
                if curr > 2 ** 31 - 1:
                    break

                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
                    break

            return False

        backtrack(0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
