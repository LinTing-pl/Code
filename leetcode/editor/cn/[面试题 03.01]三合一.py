# 三合一。描述如何只用一个数组来实现三个栈。 
# 
#  你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。
# stackNum表示栈下标，value表示压入的值。 
# 
#  构造函数会传入一个stackSize参数，代表每个栈的大小。 
# 
#  示例1: 
# 
#  
#  输入：
# ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
# [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
#  输出：
# [null, null, null, 1, -1, -1, true]
# 说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
#  
# 
#  示例2: 
# 
#  
#  输入：
# ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
# [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
#  输出：
# [null, null, null, null, 2, 1, -1, -1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= stackNum <= 2 
#  
#  Related Topics 栈 设计 数组 👍 49 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class TripleInOne(object):

    def __init__(self, stackSize):
        """
        :type stackSize: int
        """
        self.stack = [[], [], []]
        self.size = stackSize

    def push(self, stackNum, value):
        """
        :type stackNum: int
        :type value: int
        :rtype: None
        """
        stack = self.stack[stackNum]
        if len(stack) < self.size:
            stack.append(value)

    def pop(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        stack = self.stack[stackNum]
        if stack:
            return stack.pop()
        return -1

    def peek(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        stack = self.stack[stackNum]
        if stack:
            return stack[-1]
        return -1

    def isEmpty(self, stackNum):
        """
        :type stackNum: int
        :rtype: bool
        """
        stack = self.stack[stackNum]
        return len(stack) == 0

    # Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
# leetcode submit region end(Prohibit modification and deletion)
