# 我们可以使用游程编码(即 RLE )来编码一个整数序列。在偶数长度 encoding ( 从 0 开始 )的游程编码数组中，对于所有偶数 i ，
# encoding[i] 告诉我们非负整数 encoding[i + 1] 在序列中重复的次数。 
# 
#  
#  例如，序列 arr = [8,8,8,5,5] 可以被编码为 encoding =[3,8,2,5] 。encoding =[3,8,0,9,2,5] 和
#  encoding =[2,8,1,8,2,5] 也是 arr 有效的 RLE 。 
#  
# 
#  给定一个游程长度的编码数组，设计一个迭代器来遍历它。 
# 
#  实现 RLEIterator 类: 
# 
#  
#  RLEIterator(int[] encoded) 用编码后的数组初始化对象。 
#  int next(int n) 以这种方式耗尽后 n 个元素并返回最后一个耗尽的元素。如果没有剩余的元素要耗尽，则返回 -1 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["RLEIterator","next","next","next","next"]
# [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
# 输出：
# [null,8,8,5,-1]
# 解释：
# RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // 这映射到序列 [8,8,
# 8,5,5]。
# rLEIterator.next(2); // 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。
# rLEIterator.next(1); // 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。
# rLEIterator.next(1); // 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。
# rLEIterator.next(2); // 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
# 但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 -1。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= encoding.length <= 1000 
#  encoding.length 为偶 
#  0 <= encoding[i] <= 10⁹ 
#  1 <= n <= 10⁹ 
#  每个测试用例调用next 不高于 1000 次 
#  
#  Related Topics 设计 数组 计数 迭代器 👍 45 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.A = encoding
        self.i = 0
        self.q = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i+1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
# leetcode submit region end(Prohibit modification and deletion)
