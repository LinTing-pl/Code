# 给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。 
# 
#  请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：favoriteCompanies = [["leetcode","google","facebook"],["google",
# "microsoft"],["google","facebook"],["google"],["amazon"]]
# 输出：[0,1,4] 
# 解释：
# favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode",
# "google","facebook"] 的子集。
# favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google",
# "facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
# 其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
#  
# 
#  示例 2： 
# 
#  输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode",
# "amazon"],["facebook","google"]]
# 输出：[0,1] 
# 解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=[
# "leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。
#  
# 
#  示例 3： 
# 
#  输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# 输出：[0,1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= favoriteCompanies.length <= 100 
#  1 <= favoriteCompanies[i].length <= 500 
#  1 <= favoriteCompanies[i][j].length <= 20 
#  favoriteCompanies[i] 中的所有字符串 各不相同 。 
#  用户收藏的公司清单也 各不相同 ，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != 
# favoriteCompanies[j] 仍然成立。 
#  所有字符串仅包含小写英文字母。 
#  
#  Related Topics 数组 哈希表 字符串 👍 28 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        result = []
        for i in range(len(favoriteCompanies)):
            if len(favoriteCompanies[i]) > 0:  # 当前的清单是否有效
                mapping = {}  # 将当前清单转化为hash表
                for c in favoriteCompanies[i]:
                    mapping[c] = 1  # 从当前清单的下一个清单开始对比
                for j in range(i + 1, len(favoriteCompanies)):
                    cnt = 0  # 当前清单与比较清单公司名字的相同的计数器
                    for fc in favoriteCompanies[j]:
                        if fc in mapping:  # 能在比较清单里找到公司名字
                            cnt += 1  # 计数器+1
                    if cnt == len(favoriteCompanies[i]):  # 判断计数器与当前清单个数相同
                        favoriteCompanies[i] = []  # 则当前清单是比较清单的子集
                        break  # 直接退出本次比较
                    if cnt == len(favoriteCompanies[j]):
                        favoriteCompanies[j] = []  # 计数器与比较清单个数相同，则比较清单是子集，当前位置直接置为空，继续下一个清单的比较
                    if j == len(favoriteCompanies) - 1:  # 能比较到最后一个清单，说明当前清单不是任何清单的子集，直接追加进result里
                        result.append(i)
        if len(favoriteCompanies[-1]) > 0:
            result.append(len(favoriteCompanies) - 1)  # 最后一个清单如果不是任何清单的子集，也需要加进来
        return result
# leetcode submit region end(Prohibit modification and deletion)
