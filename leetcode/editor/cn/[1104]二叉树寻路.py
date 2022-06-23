# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。 
# 
#  如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记； 
# 
#  而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。 
# 
#  
# 
#  给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：label = 14
# 输出：[1,3,4,14]
#  
# 
#  示例 2： 
# 
#  输入：label = 26
# 输出：[1,2,6,10,26]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= label <= 10^6 
#  
#  Related Topics 树 数学 二叉树 👍 177 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        while label != 1:
            res.append(label)
            label //= 2

        res.append(1)
        res.reverse()

        # 从倒数第二个开始，每隔一个，找出取反相对应的值
        for i in range(len(res) - 2, -1, -2):
            original = res[i]
            #
            start = 2 ** i
            end = 2 ** (i + 1) - 1
            new = start + end - original
            res[i] = new

        return res
# leetcode submit region end(Prohibit modification and deletion)
