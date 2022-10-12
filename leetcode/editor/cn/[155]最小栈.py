# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 
# 
#  实现 MinStack 类: 
# 
#  
#  MinStack() 初始化堆栈对象。 
#  void push(int val) 将元素val推入堆栈。 
#  void pop() 删除堆栈顶部的元素。 
#  int top() 获取堆栈顶部的元素。 
#  int getMin() 获取堆栈中的最小元素。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  pop、top 和 getMin 操作总是在 非空栈 上调用 
#  push, pop, top, and getMin最多被调用 3 * 10⁴ 次 
#  
#  Related Topics 栈 设计 👍 1201 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack(object):

    def __init__(self):
        self.r = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.r.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.r.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.r[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.r)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
